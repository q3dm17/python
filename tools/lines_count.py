import os
import chardet
import sys


def check_file(filename):
    with open(filename, "rb") as file:
        detection = chardet.detect(file.read())
        if detection["encoding"] != "UTF-8-SIG" or detection["confidence"] < 0.9:
            print("Bad file:\t{}\t{}".format(filename, detection["encoding"]))


def check_dir(dir_path):
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for for_check in filter(lambda file: file.endswith(".cs") and not file.startswith("TemporaryGeneratedFile_"),
                                filenames):
            check_file(os.path.join(dirpath, for_check))


def main():
    target = sys.argv[1] if len(sys.argv) > 1 else "C:\work\portal.requisites"
    print(target)
    check_dir(target)


if __name__ == "__main__":
    main()
