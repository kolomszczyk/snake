
# 1 empty
# 2 tail
# 3 head
TABLE_X, TABLE_Y = 20, 20

# matrix[x] [y]
# - x
# | y 


def create_matrix():
    return [["X" for i in range(TABLE_X)] for j in range(TABLE_Y )]



# point 
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y


