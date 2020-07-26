import curses
# To get curses on Windows: pip install windows-curses
from random import randint


def main(stdscr):
    stdscr.clear()

    # Window setup
    height = 20
    width = 50
    win = curses.newwin(height, width, 0, 0)  # window size
    win.border(0)
    win.keypad(1)  # arrow keys to control the snake
    win.nodelay(1)  # loop until new input
    win.timeout(150)
    # curses.noecho() # no other input keys
    curses.curs_set(0)  # invisible cursor

    # Initialization of the snake and item positions
    snake = [(3, 5), (3, 4), (3, 3)]
    item = (10, 25)

    win.addch(item[0], item[1], "#")

    score = 0

    KEY_ESC = 27
    key = curses.KEY_RIGHT

    # Esc key to stop
    while key != KEY_ESC:
        win.addstr(0, 1, ' Score: ' + str(score) + ' ')

        prev_key = key
        event = win.getch()
        key = event if event != -1 else prev_key

        # Listen only to arrow keys and escape key
        if key not in [curses.KEY_UP, curses.KEY_RIGHT, curses.KEY_DOWN, curses.KEY_LEFT, KEY_ESC]:
            key = prev_key

        # Do nothing if key pressed goes in the opposite direction
        if (prev_key == curses.KEY_DOWN and key == curses.KEY_UP) or (prev_key == curses.KEY_LEFT and key == curses.KEY_RIGHT) or (prev_key == curses.KEY_UP and key == curses.KEY_DOWN) or (prev_key == curses.KEY_RIGHT and key == curses.KEY_LEFT):
            key = prev_key

        # Add new head to snake
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
        
        # Continue on the other side of the board
        if y == 0:
            y = height-2
        if x == 0:
            x = width-2
        if y == height-1:
            y = 1
        if x == width-1:
            x = 1
            
        snake.insert(0, (y, x))

        # Lose when snake runs over itself
        if snake[0] in snake[1:]:
            break

        # When snake eat the item
        if snake[0] == item:
            score += 1
            item = ()
            while item == ():
                # compute new item position
                item = (randint(1, height-2), randint(1, width-2))
                if item in snake:
                    item = ()
            win.addch(item[0], item[1], "#")
        else:
            tail = snake.pop()  # cuts off snake's tail if it didn't eat the item
            win.addch(tail[0], tail[1], " ")

        win.addch(snake[0][0], snake[0][1], 'O')
    print("Score: " + str(score))

curses.wrapper(main)
