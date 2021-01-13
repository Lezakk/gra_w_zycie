import CellClass as cell


class CellFactory:

    @staticmethod
    def create_cell(x, y, state):
        if x >= 0 and y >= 0:
            return cell.Cell(x, y, state)
        else:
            raise ValueError('Tablica jest za mała!')

