import curses
# To get curses on Windows: pip install windows-curses

# window setup
curses.initscr()
win = curses.newwin(20, 20, 0, 0) # window size; return null if window > terminal
win.border(0)
win.keypad(1) # arrow keys to control the snake
win.nodelay(1) # loop until new input
curses.noecho() # no other input keys
curses.curs_set(0) # invisible cursor

# end
curses.endwin()