import curses


def main(stdscr):
    curses.mousemask(1)
    stdscr.addstr("[R] Haga clic en esta palabra.")
    while True:
        event = stdscr.getch()
        if event == curses.KEY_MOUSE:
            _, x, y, _, _ = curses.getmouse()
            clicked_word = stdscr.instr(y, x - 1, 3).decode('utf-8')

            print(clicked_word)
            # if clicked_word.strip() == "palabra":
                # curses.flash()
                # break


curses.wrapper(main)
