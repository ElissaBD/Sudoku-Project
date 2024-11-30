import pygame
from sudoku_generator import SudokuGenerator
from board import Board
from cell import Cell

width = 800
height = 800
background_color = (255, 255, 255)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sudoku")

### integrate this so it can do different cells for more modes
generator = SudokuGenerator(9, 40)
board_array = generator.get_board()

play = True
while play == True:
  if board.is_solved():
    print("You solved the puzzle!")
    play = False
    board.draw(screen)


