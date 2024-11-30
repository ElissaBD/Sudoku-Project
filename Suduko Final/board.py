import pygame
from cell import Cell

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.grid = []
        for row in range(9):
        row_cells = []
        for col in range(9):
          cell = Cell(0, row, col, self.screen)
          row_cells.append(cell)
        self.grid.append(row_cells)


    def draw(self):
        self.draw_grid()
        for row in range(9):
            for col in range(9):
                self.grid[row][col].draw()

    def draw_grid(self):
        block_size = self.width // 9
        for row in range(9):
            for col in range(9):
                ### figure this out
    def select(self, row, col):
        self.selected = (row, col)

    def click(self, x, y):
        block_size = self.width // 9
        row = y // block_size
        col = x // block_size
        if 0 <= row < 9 and 0 <= col < 9:
            return (row, col)
        return None

    def clear(self):
        if self.selected:
            row, col = sel
