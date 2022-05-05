import pygame


# some setting
MATRIX_WIDTH: int = 30
MATRIX_HEIGHT: int =  30
MATRIX_BOX_PIX: int = 25

WIDTH_PIX: int = MATRIX_WIDTH * MATRIX_BOX_PIX
HEIGHT_PIX: int = MATRIX_HEIGHT  * MATRIX_BOX_PIX 


# this function help draw 
# proper rectangles
def draw_rect(screen, color, x, y):

    pygame.draw.rect(screen, color, [x * MATRIX_BOX_PIX, 
        (MATRIX_HEIGHT - y - 1) * MATRIX_BOX_PIX,
        MATRIX_BOX_PIX,
        MATRIX_BOX_PIX])

