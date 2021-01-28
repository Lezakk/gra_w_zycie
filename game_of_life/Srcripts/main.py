from BoardFactory import BoardFactory
import PygameScript
import pygame, sys

X = 1200
Y = 800
pygame.init()
pygame_object = PygameScript.PygameBoard(X, Y)
board = BoardFactory.create_board(70, 70)
board.create_board_with_cells()


def start_game():
    while True:
        pygame_object.create_border(board)
        pygame_object.show_text_game(board)
        pygame.display.flip()
        pygame.time.delay(100)
        board.iterate_through_board_get_neighbors()
        pygame_object.draw_alive_cells_on_board(board)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                board.iterate_through_board_clear_board()
                pygame_object.draw_alive_cells_on_board(board)
                pygame.display.flip()
                menu()

def menu():
    while True:
        pygame_object.create_border(board)
        pygame.display.flip()
        pygame_object.show_text_menu(board)
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(int(x/10), int(y/10))
                board.change_state(int(x / 10), int(y / 10))
                pygame_object.draw_alive_cells_on_board(board)
                pygame.display.flip()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                start_game()

menu()