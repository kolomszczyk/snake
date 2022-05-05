import curses
from curses import wrapper
from time import sleep, time
from math import floor
from utils import *


head = Point(5, 5)

matrix = create_matrix()

score = 0

apple = Point(10, 10)

BLUE = None

def draw(stdscr):
    '''
    # copy matrix 
    matrix_copy = matrix


    for j in range(TABLE_X):
        # |
            for i in range(TABLE_Y ):
                chars =  str(matrix_copy[i][j]) 
                # if(i == apple.get_x() and j == apple.get_y()):
                #     stdscr.addstr(20, 100, "a")
                #     stdscr.addstr(apple.get_y(), apple.get_x()*3, "a")
                if chars == "X":
                    stdscr.addstr(i, j*3, chars)
                else:
                    # Color O to red
                    stdscr.addstr(i, j*3, chars, curses.color_pair(1))
    # draw apple
    # stdscr.(apple.get_y(), apple.get_x() * 3, "a")

    # score counter
    stdscr.addstr(0, TABLE_Y * 3 + 10, str(score))

    '''
    
    # Test 

    stdscr.addstr(str(last_key))

    stdscr.refresh()
    stdscr.getch()

def logic(stdscr):
    # void X
    # head O
    # tail t

    # matrix[head[0]] [head[1]] = "O"     
    # matrix[head.get_x()][head.get_y()] = "w"
    # matrix[head.get_x()][head.get_y()] = "Y"

    matrix[head.get_x()][head.get_y()] = "X"

    ui = last_key 

    # up
    if(ui == ord('w')):
        head.set_x(head.get_x() - 1)
    # down    
    if(ui == ord('s')):
        head.set_x(head.get_x() + 1)
    # left
    if(ui == ord('a')):
        head.set_y(head.get_y() - 1)
    # right 
    if(ui == ord('d')):
        head.set_y(head.get_y() + 1)
    if(ui == ord('l')):
        exit()


    matrix[head.get_x()][head.get_y()] = "O"


last_key =  1
    
def set_last_key(stdscr):
    now_key = stdscr.getch()

    # no input 
    if(now_key == curses.ERR):
        return 

    last_key = now_key
    
    # check if exit
    if last_key == ord("l"):
        pass

def main(stdscr):
    # some setting 
    curses.noecho()
    # red color 
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    # removes deley from ui 
    stdscr.nodelay(True)
    
    time_last = time()
    while(True):
        set_last_key(stdscr) 

        time_now = time() 
        if(time_now - time_last > 1):
            time_last = time_now

            logic(stdscr)
            draw(stdscr)
        
        sleep(0.1)

            



if __name__ == "__main__":
    wrapper(main)
