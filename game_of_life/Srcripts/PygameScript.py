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

    def show_text_menu(self, board):
        alive_cell_color = (255, 255, 255)
        font = pygame.font.SysFont(None, 24)
        img = font.render('Menu', True, alive_cell_color)
        self.pygame_board.blit(img, ((board.width + 10) * 10, 50))
        img = font.render('1. Zaznacz myszką żywe komórki', True, alive_cell_color)
        self.pygame_board.blit(img, ((board.width + 12) * 10, 90))
        img = font.render('2. Naciśnij spację aby zacząć symulację', True, alive_cell_color)
        self.pygame_board.blit(img, ((board.width + 12) * 10, 110))
        img = font.render('3. Wciśnij ESC aby zakończyć', True, alive_cell_color)
        self.pygame_board.blit(img, ((board.width + 12) * 10, 130))
        pygame.display.update()

    def show_text_game(self, board):
        alive_cell_color = (255, 255, 255)
        font = pygame.font.SysFont(None, 24)
        img = font.render('Menu', True, alive_cell_color)
        self.pygame_board.blit(img, ((board.width + 10) * 10, 50))
        img = font.render('1. Wciśnij ESC aby wrócić do menu', True, alive_cell_color)
        self.pygame_board.blit(img, ((board.width + 12) * 10, 90))
        pygame.display.update()

    def create_border(self, board):
        border_color = (204, 204, 204)
        for y in range(0, board.width):
            size = (board.cell_size, board.cell_size)
            pygame.draw.rect(self.pygame_board, border_color, pygame.Rect((0, y*10), size))
        for y in range(0, board.width):
            size = (board.cell_size, board.cell_size)
            pygame.draw.rect(self.pygame_board, border_color, pygame.Rect((board.width*10, y*10), size))
        for x in range(0, board.height):
            size = (board.cell_size, board.cell_size)
            pygame.draw.rect(self.pygame_board, border_color, pygame.Rect((x * 10, 0), size))
        for x in range(0, board.width):
            size = (board.cell_size, board.cell_size)
            pygame.draw.rect(self.pygame_board, border_color, pygame.Rect((x * 10, board.height * 10), size))

