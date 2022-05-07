import pygame
from time import sleep
import time
from snake import * 
from utils import *


# g stands for grass
# b stands for body
# h stands for head of snake 
# a stands for apple 

matrix = [["g" for _ in range(MATRIX_HEIGHT)] for _ in range(MATRIX_WIDTH)]

# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)




def draw(screen: pygame.surface.Surface, snake: Snake):
    screen.fill(BLUE)

    # for every cell in matrix
    for width in range(MATRIX_WIDTH):
        for height in range(MATRIX_HEIGHT):
            # get color of cell
            
            # default color 
            color = BLACK
            # body 
            if matrix[width][height] == "b":
                color = GREEN
            # head of snake
            if matrix[width][height] == "h":
                color = WHITE
            # apple
            if matrix[width][height] == "a":
                color = RED
                

            # draw this cell 
            draw_rect(screen, color, width, height)



    # apple        
    draw_rect(screen, RED, snake.apple_x, snake.apple_y)

    # draw snake
    # head
    draw_rect(screen, BLUE, snake.head_x, snake.head_y)
    # body
    for point in snake.body:
        draw_rect(screen, GREEN, point[0], point[1])
    



    # refresh 
    pygame.display.flip()
    

def tick(snake: Snake) -> bool:


    stop_game = snake.is_next_move_collision()

    # if stop game
    # dont draw last frame
    if stop_game == False:
        return stop_game
        
    snake.move(snake.direction)



    return stop_game



def main():

    pygame.init()

    # create a surface on screen that has the size of WIDTH x HEIGHT
    screen = pygame.display.set_mode((WIDTH_PIX, HEIGHT_PIX))

    snake: Snake = Snake(15, 15)

    running = True
   
    t0 = time.time()

    # main loop
    while(running):
        
         
        

        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do somthing if the event is of type QUIT
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
            # set snake direction
                if event.key == pygame.K_a:
                    snake.set_direction("left")
                if event.key == pygame.K_d:
                    snake.set_direction("right")
                if event.key == pygame.K_w:
                    snake.set_direction("up")
                if event.key == pygame.K_s:
                    snake.set_direction("down")


        # run tick fucntion
        # every 1 s 
        t1 = time.time()        
        if(t1 - t0 >= 0.5):
            # reset clock
            t0 = t1
            running = tick(snake)

        
        draw(screen, snake)

    game_end()

if __name__ == "__main__":
    main()



