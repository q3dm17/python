import curses
from curses import wrapper

from collect import calc_stats


def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    start_path = R"/mnt/c/Users/s.rozhin/study/"
    stats = calc_stats(start_path)

    def print_dirs():
        dirs = stats.GetTopDirs(5)
        stdscr.addstr(0, 0, "{}".format(stats.current_directory.path), curses.color_pair(1))
        for y in range(len(dirs)):
            stdscr.addstr(y + 1, 0, "{}\t{} in '{}'".format(dirs[y].total_size, dirs[y].files_size, dirs[y].path))
        stdscr.refresh()

    def handle_folder_select(key):
        folder_number = int(key)-1
        if folder_number == -1:
            stats.move_up()
        else:
            dirs = stats.GetTopDirs(5)
            stats.move_to(dirs[folder_number].path)

    prev_key = None
    while True:
        if prev_key:
            if prev_key == "Q":
                stdscr.clear()
                stdscr.addstr("quitting")
                stdscr.addstr("\npress any key to exit")
                stdscr.refresh()
                stdscr.getkey()
                break
            else:
                if prev_key in {"1","2","3","4","5","0"}:
                    handle_folder_select(prev_key)
        print_dirs()
        stdscr.refresh()
        prev_key = stdscr.getkey()
        stdscr.clear()


wrapper(main)
