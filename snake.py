

class Snake():




    # left right,
    # up down
    direction: str = "left"


    def __init__(self, x:int, y: int):
        self.head_x = x
        self.head_y = y


    def set_direction(self, directection:str):
        self.direction = directection

    def move(self, direction: str):
        pass


