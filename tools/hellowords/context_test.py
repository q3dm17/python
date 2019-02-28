import time
import tempfile
from contextlib import redirect_stdout
from contextlib import ExitStack

import io


class StopWatchLog:
    def __enter__(self):
        self.start = time.clock()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Func time is %f" % (time.clock() - self.start))

    def log(self, msg):
        print("{}:\t{}".format(time.clock() - self.start, msg))


def merge_logs(output_path, *log_paths):
    with ExitStack() as stack:
        handles = [stack.enter_context(open(log_path)) for log_path in log_paths]
        output = open(output_path, "wt")
        stack.enter_context(output)
        for handle in handles:
            output.write(handle.read())


if __name__ == "__main__":
    with StopWatchLog() as log:
        log.log("Starting sleep")
        time.sleep(0.25)
        log.log("Finished sleep")

    with tempfile.TemporaryFile() as handle:
        path = handle.name
        print(path)

    handle = io.StringIO()
    with redirect_stdout(handle):
        print("Hello, world")
    print("Given: " + handle.getvalue())
