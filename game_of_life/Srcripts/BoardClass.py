from CellClass import Cell
from CellFactory import CellFactory
import pygame


class Board:
    board = []

    def __init__(self, width, height, cell_size=10):
        self.width = width
        self.height = height
        self.cell_size = cell_size

    def create_board_with_cells(self):
        for x in range(1, self.width-1):
            row = []
            for y in range(1, self.height-1):
                row.append(CellFactory.create_cell(x, y, False))
            self.board.append(row)

    def print_board(self):
        for col in range(len(self.board)):
            for row in range(len(self.board[col])):
                print(self.board[col][row].get_state())
            print()

    def get_neighbors(self, x, y):
        counter = 0
        for col in range(x - 1, x + 2):
            for row in range(y - 1, y + 2):
                if col == x and row == y:
                    continue
                if self.board[col][row].get_state():
                    counter += 1
        if counter == 3:
            self.board[x][y].set_state(True)
        elif counter == 2:
            self.board[x][y].get_state()
        else:
            self.board[x][y].set_state(False)

    def iterate_through_board_get_neighbors(self):
        for col in range(1, len(self.board) - 1):
            for row in range(1, len(self.board[col]) - 1):
                self.get_neighbors(col, row)

    def iterate_through_board_get_alive_cells(self):
        for col in range(1, len(self.board) - 1):
            for row in range(1, len(self.board[col]) - 1):
                if self.board[col][row].get_state():
                    yield col, row

    def change_state(self, x, y):
        state = self.board[x][y].get_state()
        if state:
            self.board[x][y].set_state(False)
        elif state is False:
            self.board[x][y].set_state(True)

    def handle_mouse(self):
        buttons = pygame.mouse.get_pressed()
        if not any(buttons):
            return
        click = True if buttons[0] else False
        x, y = pygame.mouse.get_pos()

        x /= self.cell_size
        y /= self.cell_size

        if click:
            self.board[int(x)][int(y)].change_state(int(x), int(y))