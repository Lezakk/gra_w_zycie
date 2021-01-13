import BoardClass as board


class BoardFactory:
    @staticmethod
    def create_board(x, y):
        if x > 2 and y > 2:
            return board.Board(x, y)
        else:
            raise ValueError('Tablica jest za mała!')