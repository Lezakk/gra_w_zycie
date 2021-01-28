import pygame, sys
import BoardClass


class PygameBoard():
    def __init__(self, width, height):
        self.pygame_board = pygame.display.set_mode(size=(width, height))

    def draw_alive_cells_on_board(self, board):
        alive_cell_color = (255,255,255)
        background_color = (0, 0, 0)
        self.pygame_board.fill(background_color)
        for x, y in board.iterate_through_board_get_alive_cells():
            size = (board.cell_size, board.cell_size)
            position = (x * board.cell_size, y * board.cell_size)
            pygame.draw.rect(self.pygame_board, alive_cell_color, pygame.Rect(position, size))

