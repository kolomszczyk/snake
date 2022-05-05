import pygame

WIDTH, HEIGHT = 320, 240
black = 255, 255, 255 

def draw(screen: pygame.surface.Surface):
    screen.fill(black)



def main():

    pygame.init()

    # create a surface on screen that has the size of WIDTH x HEIGHT
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

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



