import os
from typing import Dict
from os.path import join, getsize


class Dir:
    def __init__(self, path: str):
        self.path = path
        self.dirs = []
        self.files_size = 0
        self.total_size = 0


def update_stats_recursively(start_dir: Dir) -> int:
    size = start_dir.files_size
    for d in start_dir.dirs:
        size += update_stats_recursively(d)
    start_dir.total_size = size
    return size


def calc_stats(stat_path: str) -> Dict[str, Dir]:
    all_dirs = {}
    for root, dirs, files in os.walk(stat_path):
        try:
            size = sum(getsize(join(root, name)) for name in files)
        except (PermissionError,OSError):
            size = 0
        d = Dir(root)
        d.files_size = size
        all_dirs[root] = d
        if '.git' in dirs:
            dirs.remove('.git')  # don't visit .git directories
        parent_path = os.path.dirname(root)

        if parent_path in all_dirs:
            all_dirs[parent_path].dirs.append(d)

    update_stats_recursively(all_dirs[stat_path])
    return all_dirs


if __name__ == '__main__':
    start_path = R'C:\Users\s.rozhin\study'
    all = calc_stats(start_path)
    print("Total size of '{}' is {}".format(start_path,all[start_path].total_size))
    threshold = (1<<25) * 10
    for d in sorted(all.values(),key=lambda x:x.total_size,reverse=True)[:5]:
        if d.total_size> threshold:
            print("{} in '{}'".format(d.total_size,d.path))
