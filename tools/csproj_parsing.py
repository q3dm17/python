import os
import argparse
from os.path import relpath
from os.path import join
import xml.etree.ElementTree as ET

__author__ = 's.rozhin'


class CsProjectParsed:
    def __init__(self, file_path):
        self.cs_files_set = CsProjectParsed.__extract_file_names_from_csproj(file_path)
        self.folder = os.path.dirname(file_path)

    @staticmethod
    def __extract_file_names_from_csproj(csproj_file_path):
        xml_csproj = ET.parse(csproj_file_path)
        xml_root = xml_csproj.getroot()
        file_set = set()
        for child in xml_root.iter():
            if 'Include' in child.attrib:
                file_set.add(child.attrib['Include'].lower())
        return file_set

    @staticmethod
    def __is_cs_file(filename):
        return filename.endswith('.cs')

    def _get_all_unincluded_files(self):
        for current_dir, dirs, files in os.walk(self.folder):
            for file_name in files:
                if CsProjectParsed.__is_cs_file(file_name):
                    # Because relpath("foo/bar","foo/bar") returns "."; i don't know, how to fix it easier
                    if current_dir == self.folder:
                        relative_path = file_name
                    else:
                        relative_path = join(relpath(current_dir, self.folder), file_name)
                    if relative_path.lower() not in self.cs_files_set:
                        yield join(current_dir, file_name)

    def print_unincluded_cs_files(self):
        for unincluded_file in self._get_all_unincluded_files():
            print unincluded_file

    def remove_unincluded_cs_files(self, print_deleting):
        for unincluded_file in self._get_all_unincluded_files():
            os.remove(unincluded_file)
            if print_deleting:
                print unincluded_file


class CsProjectSearcher:
    def __init__(self):
        pass

    @staticmethod
    def find_from_directory(start_folder):
        for current_dir, dirs, files in os.walk(start_folder):
            for file_name in files:
                if CsProjectSearcher.is_csproj_file(file_name):
                    yield CsProjectParsed(join(current_dir, file_name))

    @staticmethod
    def is_csproj_file(filename):
        return filename.endswith('.csproj')


def print_only(path):
    print 'printing only for path: ' + path
    for project in CsProjectSearcher.find_from_directory(path):
        project.print_unincluded_cs_files()


def remove_from_path(path, print_deleting=False):
    print 'cleaning for path: ' + path
    for project in CsProjectSearcher.find_from_directory(path):
        project.remove_unincluded_cs_files(print_deleting)


def main():
    parser = argparse.ArgumentParser(description='Detect and optionally delete not included in projects cs files.')
    parser.add_argument("repository_path", help='Start folder for searching cs project and cs source files')
    action_group = parser.add_mutually_exclusive_group()
    action_group.add_argument("-s", "--show", action="store_true",
                              help="print files only without deleting")
    action_group.add_argument("-r", "--remove", action="store_true",
                              help="delete files")
    parser.add_argument("-v", "--verbose", help="Print deleted files",
                        action="store_true")
    args = parser.parse_args()

    if args.show:
        print_only(args.repository_path)
    elif args.remove:
        remove_from_path(args.repository_path, args.verbose)


main()