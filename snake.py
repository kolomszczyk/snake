import random
from utils import MATRIX_WIDTH, MATRIX_HEIGHT


class Snake():

    body = []

    # left right,
    # up down
    direction: str = "left"

    def __init__(self, x: int, y: int):
        self.head_x = x
        self.head_y = y

        self.apple_x = 0
        self.apple_y = 0
        self.generate_next_apple()

        self.score = 0

    def set_direction(self, directection: str):
        self.direction = directection

    def move(self, direction: str):

        # if head of snake is on apple
        # dont pop last part of body
        is_head_on_apple = False
        if self.head_x == self.apple_x and self.head_y == self.apple_y:

            self.generate_next_apple()
            is_head_on_apple = True
            self.score += 1
            print(f"score: {self.score}")

        # moves body
        self.body.append((self.head_x, self.head_y))
        # when snake start the game
        # it starts from single point
        # this code makes starts prety
        if(len(self.body) >= 3 and is_head_on_apple == False):
            # normal
            self.body.pop(0)

        # moves head
        if direction == "up":
            self.head_y += 1
        if direction == "down":
            self.head_y -= 1
        if direction == "left":
            self.head_x -= 1
        if direction == "right":
            self.head_x += 1



    def is_next_move_collision(self) -> bool:
        # next_head_posision_x
        nhp_x = self.head_x
        # next_head_posision_y
        nhp_y = self.head_y

        # calculate next posision of head
        if self.direction == "up":
            nhp_y += 1
        if self.direction == "down":
            nhp_y -= 1
        if self.direction == "left":
            nhp_x -= 1
        if self.direction == "right":
            nhp_x += 1

        # matrix border
        if nhp_x < 0 or nhp_x >= MATRIX_WIDTH or nhp_y < 0 or nhp_y >= MATRIX_HEIGHT:
            return False

        # snake body
        for body in self.body:
            if body[0] == nhp_x and body[1] == nhp_y:
                return False

        # snake body

        return True

    # apple stuf

    def generate_next_apple(self):
        # do while apple is on other place then head not body
        # to do:
        # - dont allow apple to spawn on body
        local_is_head_on_apple: bool = True
        while(local_is_head_on_apple):
            self.apple_x = random.randint(0, MATRIX_WIDTH - 1)
            self.apple_y = random.randint(0, MATRIX_HEIGHT - 1)
            if self.apple_x != self.head_x and self.apple_y != self.head_y:
                local_is_head_on_apple = False

        print(f"apple x:{self.apple_x} y:{self.apple_y}")











