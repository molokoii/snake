import curses
# To get curses on Windows: pip install windows-curses

def main(stdscr):
    stdscr.clear()

    # Window setup
    win = curses.newwin(20, 50, 0, 0) # window size - return null if window > terminal
    win.border(0)
    win.keypad(1) # arrow keys to control the snake
    win.nodelay(1) # loop until new input
    #curses.noecho() # no other input keys
    curses.curs_set(0) # invisible cursor

    snake = [(3,3), (3,2), (3,1)]
    item = (10, 10)

    win.addch(item[0], item[1], "#")

    ESC = 27
    event = win.getch()

    while event != ESC:
        event = win.getch()

        for c in snake:
            win.addch(c[0], c[1], "O")
        
        win.addch(item[0], item[1], "#")
    
    # End
    # win.refresh()
    # win.getkey()

curses.wrapper(main)
