import pygame
from time import sleep

MATRIX_WIDTH: int = 30
MATRIX_HEIGHT: int =  30
MATRIX_BOX_PIX: int = 25

WIDTH_PIX: int = MATRIX_WIDTH * MATRIX_BOX_PIX
HEIGHT_PIX: int = MATRIX_HEIGHT  * MATRIX_BOX_PIX 


# g stands for grass
# b stands for body
# h stands for head of snake 
# a stands for apple 

matrix = [["g" for i in range(MATRIX_HEIGHT)] for j in range(MATRIX_WIDTH)]
matrix[0][0] = "b"
matrix[1][1] = "h"
matrix[2][2] = "a"

# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
 


def draw(screen: pygame.surface.Surface):
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
            pygame.draw.rect(screen, color, [width * MATRIX_BOX_PIX, 
                (MATRIX_HEIGHT - height - 1) * MATRIX_BOX_PIX,
                MATRIX_BOX_PIX,
                MATRIX_BOX_PIX])
    
    # refresh 
    pygame.display.flip()



def main():

    pygame.init()

    # create a surface on screen that has the size of WIDTH x HEIGHT
    screen = pygame.display.set_mode((WIDTH_PIX, HEIGHT_PIX))

    running = True
   
    # main loop
    while(running):

        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do somthing if the event is of type QUIT
            if event.type == pygame.QUIT:
                running = False

        
        draw(screen)
        

if __name__ == "__main__":
    main()



