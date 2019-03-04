import curses
from curses import wrapper

def main(stdscr):
    # Clear screen
    stdscr.clear()
#    stdscr.addstr(0, 0, "Current mode: Typing mode",
#                  curses.A_REVERSE)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_GREEN)
    stdscr.addstr("Pretty text", curses.color_pair(1))
    stdscr.refresh()
    stdscr.getkey()

    begin_x = 20; begin_y = 7
    height = 5; width = 40
#    win = curses.newwin(height, width, begin_y, begin_x)

    prev_key = None
    for i in range(0, 10):
        v = i-10
        stdscr.clear()
        stdscr.refresh()
        stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v))
        if prev_key:
            if prev_key == "Q":
                stdscr.addstr("quitting")
                stdscr.addstr("press any key to exit")
                stdscr.refresh()
                stdscr.getkey()
                break
            else:
                stdscr.addstr("Previously pressed: " + prev_key)
        stdscr.refresh()
        prev_key = stdscr.getkey()

wrapper(main)