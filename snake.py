import random
from utils import MATRIX_WIDTH, MATRIX_HEIGHT

class Snake():

    body = [] 
            

    lenght = 0

    # left right,
    # up down
    direction: str = "left"


    def __init__(self, x:int, y: int):
        self.head_x = x
        self.head_y = y

        self.apple_x = 0
        self.apple_y = 0
        self.generate_next_apple()

        self.score = 0

    def set_direction(self, directection:str):
        self.direction = directection

    def move(self, direction: str):

        # if head of snake is on apple 
        # dont pop last part of body    
        # add to lenght
        is_head_on_apple = False
        if self.head_x == self.apple_x and self.head_y == self.apple_y:
            
            self.generate_next_apple()
            is_head_on_apple = True
            self.lenght += 1
            self.score += 1
            print(f"score: {self.score}")



        # moves body
        self.body.append((self.head_x, self.head_y))
        # when snake start the game 
        # it starts from single point   
        # this code makes starts prety
        if(self.lenght >= 3 and is_head_on_apple == False):
            self.body.pop(0)
        

        else:
            self.lenght += 1

        # moves head 
        if direction == "up":
            self.head_y += 1
        if direction == "down":
            self.head_y -= 1
        if direction == "left":
            self.head_x -= 1
        if direction == "right":
            self.head_x += 1


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




        






