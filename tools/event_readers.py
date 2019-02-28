import re


class LogProcessor():
    def __init__(self, file_name):
        self.file_name = file_name
        self.__trace_ids = set()
        self.__user_ids = set()

    def __handle_credentials(self, line):
        trace = self.__get_trace_id(line)
        if trace in self.__trace_ids:
            self.__user_ids.add(line[line.find("user id = ")+10:line.find("user id = ")+46])
            self.__trace_ids.remove(trace)

    def __handle_start(self, line):
        trace = self.__get_trace_id(line)

        self.__trace_ids.add(trace)

    def __get_trace_id(self, line):
        return re.search(r"\[T-[0-9a-f]{8}\([-,+]\)]", line).group(0)

    def process_log(self):
        with open(self.file_name, "r", -1) as file:
            for line in file:
                if line.find("/events") != -1:
                    self.__handle_start(line)
                elif line.find("Authenticated service =") != -1:
                    self.__handle_credentials(line)
        print("Found users for event reading")
        print("\n".join(self.__user_ids))
        print("Not found trace ids")
        for trace in self.__trace_ids:
            print(trace)

LogProcessor(R"C:\Users\s.rozhin\work\event_readers\res.txt").process_log()