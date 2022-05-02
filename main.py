from package import *

from PIL import Image
#import pygame

WIN = pygame.display.set_mode((WIDTH, HEIGHT)) #set up pygame window
pygame.display.set_caption("Pixel Art App")

#displays the grid/canvas and the gridlines on the screen 
def canvas(win, grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(win, pixel, (j * PIXEL_SIZE, i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE)) #where, color, coordinates

    if GRID_LINES:
        for i in range(N+1):
            pygame.draw.line(win, BLACK, (0, i*PIXEL_SIZE),  (WIDTH, i*PIXEL_SIZE))

        for i in range(M+1):
            pygame.draw.line(win, BLACK, (i*PIXEL_SIZE, 0),  (i*PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))


#creates a grid and initalizes/fills it with the given color (which is the background color)
def init_grid(n, m, color):
    grid = [] #2D list, list of lists, each element is a tuple with the RGB colors of the pixel

    #fill 2D list with colors
    for i in range(n):
        grid.append([])
        for j in range(m):
            grid[i].append(color)
    
    return grid


#fill window with base color + display grid via calling another function, display buttons
def display(win, grid, buttons):
    win.fill((230, 230, 250))
    canvas(win, grid)

    for button in buttons:
        button.draw(win)

    pygame.display.update()


#determines on which pixel did the mouse click, raises error if clicked outside the grid/canvas
def get_gridpixel_from_posm(posm):
    x, y = posm
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE

    if row >= N:
        raise IndexError #clicked outside of canvas

    return row, col

ok=True

clock = pygame.time.Clock()

#makes grid in main function
grid = init_grid(N, M, BG_COLOR)
drawing_color = BLACK

button_y= HEIGHT - TOOLBAR_HEIGHT/2 - 25 #25 is half the height of button
buttons = [ 
    Button(10, button_y, 50, 50, BLACK),
    Button(70, button_y, 50, 50, WHITE), # 10 + length of button + 10
    Button(130, button_y, 50, 50, RED),
    Button(190, button_y, 50, 50, GREEN),
    Button(250, button_y, 50, 50, BLUE),
    Button(310, button_y, 50, 50, YELLOW),
    Button(370, button_y, 50, 50, WHITE, "Eraser", BLACK),
    Button(430, button_y, 50, 50, WHITE, "Clear", BLACK),
    Button(490, button_y, 50, 50, WHITE, "Save", BLACK),
    Button(550, button_y, 50, 50, WHITE, "Load", BLACK)
]

while ok:
    clock.tick(FPS) #assures frame consistency

    #program ends when user presses X button
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            ok=False

        pencil=True
        click=False

        if pygame.mouse.get_pressed()[0]: #check if user left clicks, [2] is right click
            posm = pygame.mouse.get_pos() #position of the mouse
            pencil=True
            click=True

        # RIGHT CLICK can be used as eraser too, but there is also an Eraser button that works with left click
        # BUTTONS CAN BE CLICKED WITH BOTH CLICKS
        if pygame.mouse.get_pressed()[2]:
            posm = pygame.mouse.get_pos()
            pencil=False
            click=True

        if click:
            try:
                row, col = get_gridpixel_from_posm(posm)

                if pencil:
                    grid[row][col]=drawing_color

                if not pencil:
                    grid[row][col]=BG_COLOR
            except IndexError: #checks if buttons have been clicked
                for button in buttons:
                    if not button.pressed(posm):
                        continue

                    if button.text == "Clear":
                        grid = init_grid(N, M, BG_COLOR)
                        
                    elif button.text == "Save":
                        image = Image.new("RGB", (M, N))
                        pixels = image.load() #returns a list of lists with tuples (RGB) inside
                        pixels[0, 0] = BG_COLOR

                        for w in range(M):
                            for h in range(N):
                                    pixels[w, h] = grid[h][w]
                        image.save("save.png")

                    elif button.text== "Load":
                        image = Image.open("save.png")
                        pixels = image.load()
                        grid = [[pixels[w, h] for w in range(M)] for h in range(N)]

                    elif button.text== "Eraser":
                        drawing_color = BG_COLOR  
                    else:
                        drawing_color = button.color

                    break

    display(WIN, grid, buttons)

pygame.quit()