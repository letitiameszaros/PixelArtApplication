import pygame
pygame.init()
pygame.font.init()

#colors for painting
WHITE = (255, 255, 255)
BLACK = (0 ,0 ,0)
RED = (255, 0 ,0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


#game window size, can be changed with certain values only
WIDTH, HEIGHT = 650, 750 #extra space for toolbar

# rows = N, columns = M
# can be changed here with certain values only
N=M=50 #individual pixels

TOOLBAR_HEIGHT= HEIGHT-WIDTH

FPS=120

PIXEL_SIZE = WIDTH // N #size of the pixels

#background color of the canvas, CAN BE CHANGED HERE
# Eraser adapts to background color change!
BG_COLOR=BLACK

#Grid lines around the pixels of the canvas, CAN BE TURNED OFF with False
GRID_LINES = True

def get_font(size):
    return pygame.font.SysFont("arial", size) #font style can be changed here