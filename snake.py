import curses
# To get curses on Windows: pip install windows-curses
from random import randint

def main(stdscr):
    stdscr.clear()

    # Window setup
    win = curses.newwin(20, 50, 0, 0)  # window size
    win.border(0)
    win.keypad(1)  # arrow keys to control the snake
    win.nodelay(1)  # loop until new input
    win.timeout(150)
    # curses.noecho() # no other input keys
    curses.curs_set(0)  # invisible cursor

    snake = [(3, 5), (3, 4), (3, 3)]
    item = (10, 10)

    win.addch(item[0], item[1], "#")

    KEY_ESC = 27
    key = curses.KEY_RIGHT

    while key != KEY_ESC:

        prev_key = key
        event = win.getch()
        key = event if event != -1 else prev_key

        if key not in [curses.KEY_UP, curses.KEY_RIGHT, curses.KEY_DOWN, curses.KEY_LEFT, KEY_ESC]:
            key = prev_key
        if (prev_key == curses.KEY_DOWN and key == curses.KEY_UP) or (prev_key == curses.KEY_LEFT and key == curses.KEY_RIGHT) or (prev_key == curses.KEY_UP and key == curses.KEY_DOWN) or (prev_key == curses.KEY_RIGHT and key == curses.KEY_LEFT):
            key = prev_key

        # Compute the next snake position
        y = snake[0][0]
        x = snake[0][1]

        if key == curses.KEY_UP:
            y -= 1
        if key == curses.KEY_RIGHT:
            x += 1
        if key == curses.KEY_DOWN:
            y += 1
        if key == curses.KEY_LEFT:
            x -= 1

        snake.insert(0, (y, x))

        if y == 0:
            break
        if y == 19:
            break
        if x == 0:
            break
        if x == 49:
            break

        if snake[0] in snake[1:]:
            break

        if snake[0] == item:
            item = ()
            while item == ():
                item = (randint(1, 18), randint(1, 48))
                if item in snake:
                    item = ()
            win.addch(item[0], item[1], "#")
            
        prev_tail = snake.pop()
        win.addch(prev_tail[0], prev_tail[1], " ")

        win.addch(snake[0][0], snake[0][1], 'O')

    # End
    # win.refresh()
    # win.getkey()


curses.wrapper(main)
