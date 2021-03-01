import pygame

class mistake():

    def __init__(self, color, radius, width):
        self.color = color
        self.radius = radius
        self.width = width
        self.name = "Brush"
    
    def setRadius(self, radius):
        self.radius = radius

    def setColor(self, color):
        self.color = color

    def setWidth(self, width):
        self.width = width

class normalBrush(mistake):
    def __init__(self, color, radius, width):
        super().__init__(color, radius, width)
        

    def draw(self, display, pos):
        pygame.draw.circle(display, self.color, pos, self.radius, self.width)


class squareBrush():
    def __init__(self, color, radius):
        self.color = color 
        self.radius = radius
        self.name = "square brush"

    def setRadius(self, radius):
        self.radius = radius

    def setColor(self, color):
        self.color = color

    def draw(self, display, pos):
        x, y = pos
        print(x, y)
        pygame.draw.rect(display, self.color, (x - self.radius / 2, y - self.radius / 2, self.radius, self.radius))

class Eraser():
    def __init__(self, radius):
        self.radius = radius
        self.name = "Rubber"
        
    def setRadius(self, radius):
        self.radius = radius

    def draw(self, display, pos):
        pygame.draw.circle(display, (225, 229, 235), pos, self.radius, 0)

    
    
    