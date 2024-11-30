import pygame

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        width = self.screen.get_width()
        height = self.screen.get
        gap = width // 9
        x = self.col * gap
        y = self.row * gap
        color = (255, 0, 0) 
        pygame.draw.rect(self.screen, color, (x, y, gap, gap), 2)

