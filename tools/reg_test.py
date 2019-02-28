import re


def main():
    pattern = re.compile(r"Reqs")
    with open("C:\logs\Cabinet\log2016.09.19", buffering=1024 * 1024) as file_handle:
        for n, line in enumerate(file_handle):
            found = pattern.findall(line)
            if len(found) != 0:
                print(line)


if __name__ == "__main__":
    main()
