from .settings import*

class Button:
    def __init__(self, x, y, width, height, color, text=None, text_color=BLACK):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.text_color = text_color

    def draw(self, win): #show button
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

        pygame.draw.rect(win, BLACK, (self.x, self.y, self.width, self.height), 3) #outlines the button with black lines

        #displays text in center of the button
        if self.text:
            button_font = get_font(18) #font size
            text_surface = button_font.render(self.text, 1, self.text_color)
            win.blit(text_surface, (self.x + self.width/2 - text_surface.get_width()/2, self.y + self.height/2 - text_surface.get_height()/2)) #position text



    def pressed(self, pos): #check if button has been clicked
        x, y = pos

        if not( x >= self.x and x <= self.x + self.width):
            return False
        if not not( y >= self.x and y <= self.x + self.height):
            return False

        return True
