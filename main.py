import pygame
from time import sleep

MATRIX_WIDTH: int = 30
MATRIX_HEIGHT: int =  30
MATRIX_BOX_PIX: int = 25

WIDTH_PIX: int = MATRIX_WIDTH * MATRIX_BOX_PIX
HEIGHT_PIX: int = MATRIX_HEIGHT  * MATRIX_BOX_PIX 

matrix = [["0" for i in range(MATRIX_HEIGHT)] for j in range(MATRIX_WIDTH)]
matrix[0][0] = "g"

# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
 


def draw(screen: pygame.surface.Surface):
    screen.fill(BLUE)
    
    # width = MATRIX_WIDTH
    # height = MATRIX_HEIGHT

    for width in range(MATRIX_WIDTH):
        for height in range(MATRIX_HEIGHT):


            pygame.draw.rect(screen, GREEN, [width * MATRIX_BOX_PIX, 
                (MATRIX_HEIGHT - height - 1) * MATRIX_BOX_PIX,
                MATRIX_BOX_PIX,
                MATRIX_BOX_PIX])
    
    # refresh ? 
            pygame.display.flip()
            print(width, height)

            sleep(0.1)



    # pygame.draw.rect(screen, GREEN, [start_x, start_y, 50, 50])
    # pygame.draw.rect(screen, GREEN, [100, 0, 50, 50])

    ''' 
    for width in range(MATRIX_WIDTH):
        for height in range(MATRIX_HEIGHT, 0, -1):
            color = GREEN
            if matrix[width-1][height-1] == "g":
                print("g")
                color = RED


            pygame.draw.rect(screen, color, [width*25, height*25, 50, 50])

            print(width, height)
            if matrix[width- 1][height -1 ] == "g":
                print(width, height)
            pygame.display.flip()
            sleep(0.05)
    '''


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



