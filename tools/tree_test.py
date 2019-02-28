# coding=utf-8
import codecs
import os
from os.path import getsize, join
dirs_description = []
with open('graph.txt', 'w', encoding='utf-8') as f:
    for root, dirs, files in os.walk(R"C:\Users\s.rozhin\Downloads"):
        root_folder_name = os.path.split(root)[1]
        for directory in dirs:
            f.write("{} -> {}\n".format(root_folder_name, directory))
        for file in files:
            f.writelines("{} -> {}\n".format(root_folder_name, file))
        root_folder_size = sum(getsize(join(root, name)) for name in files)
        dirs_description.append("{0} {{label: {0}({1})}}\n".format(root_folder_name, root_folder_size))
    for dir_desc in dirs_description:
        f.write(dir_desc)
