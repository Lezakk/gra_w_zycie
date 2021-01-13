from BoardFactory import BoardFactory
import PygameScript
import pygame, sys

pygame.init()

pygame_object = PygameScript.Pygame_board(980, 980)

board = BoardFactory.create_board(9, 12)
board.create_board_with_cells()
for x in range(7):
    for y in range(7):
        board.board[x][y].set_state(True)
# board.board[10][10].set_state(True)
# board.board[10][11].set_state(True)
# board.board[10][12].set_state(True)
# board.board[10][13].set_state(True)
# board.board[10][14].set_state(True)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit(0)


    pygame.time.delay(500)
    board.iterate_through_board_get_neighbors()
    pygame_object.draw_alive_cells_on_board(board)
    pygame.display.flip()
    pygame.time.delay(500)


# board.print_board()
# print("--------------------------------")
# board.iterate_through_board()
# board.iterate_through_board()
#
# board.print_board()