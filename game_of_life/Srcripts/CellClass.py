class Cell:
    def __init__(self, x, y, state):
        self.__x = x
        self.__y = y
        self.__state = state

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_state(self):
        return self.__state

    def set_state(self, state):
        self.__state = state
