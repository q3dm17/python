import os
from typing import Dict, List
from os.path import join, getsize


class Dir:
    def __init__(self, path: str):
        self.path = path
        self.dirs = []
        self.files_size = 0
        self.total_size = 0


class DiscUsageStats:
    def __init__(self, start_path: str, dirs: Dict[str, Dir]):
        self.directories = dirs
        self.current_dir_path = start_path
        self.start_path = start_path

    def GetTopDirs(self, count: int)->List[Dir]:
        current_dir = self.directories[self.current_dir_path]
        return sorted(current_dir.dirs, key=lambda x: x.total_size, reverse=True)[:count]

    @property
    def current_directory(self)->Dir:
        return self.directories[self.current_dir_path]

    def move_to(self, dir_path: str):
        # todo add check for dir_path correctness
        self.current_dir_path = dir_path

    def move_up(self):
        if self.current_dir_path != self.start_path:
            self.current_dir_path = os.path.dirname(self.current_dir_path)




def update_stats_recursively(start_dir: Dir) -> int:
    size = start_dir.files_size
    for d in start_dir.dirs:
        size += update_stats_recursively(d)
    start_dir.total_size = size
    return size


def calc_stats(stat_path: str) -> DiscUsageStats:
    stat_path = stat_path.rstrip("\\").rstrip("/")
    all_dirs = {}
    for root, dirs, files in os.walk(stat_path):
        try:
            size = sum(getsize(join(root, name)) for name in files)
        except (PermissionError, OSError):
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
    return DiscUsageStats(stat_path, all_dirs)


if __name__ == '__main__':
    start = R'C:\Users\s.rozhin\study'
    stats = calc_stats(start)
    print("{}\tis total size of '{}'".format(start, stats.current_directory.total_size))
    threshold = 0#(1 << 25) * 10
    for d in stats.GetTopDirs(50):
        if d.total_size > threshold:
            print("{}\tin\t'{}'".format(d.total_size, d.path))
