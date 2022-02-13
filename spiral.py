# ToDo: 1) See if x and y co-ordinates can be represented as a data class.
# ToDo: 2) eliminate the need for a limit parameter to traverse spiral


def create_spiral(n):
    class Matrix:

        def __init__(self, size):
            self.size = size
            self.value = 0
            self.matrix = self.init_matrix(size)
            self.dirmap = {'right': 1, 'down': 1, 'left': -1, 'up': -1}

        def init_matrix(self, x):
            return [[0 for i in range(x)] for i in range(x)]

        def get_matrix(self):
            return self.matrix

        def get_value(self):
            return self.value

        def get_dirmap(self):
            return self.dirmap

        def set_value(self, value):
            self.value = value

        def inc_value(self, inc=1):
            self.value += inc

        def setxy_to_value(self, x, y, value):
            self.matrix[x][y] = value

    def traverse_spiral(matrix, x, y, direction, limit):
        """
        :param matrix: Matrix object to process
        :param x: starting row
        :param y: starting col
        :param direction: Direction to start filling
        :param limit: row or column value to mark the limit of current fill.
        :return: the x,y location of the last fill.
        """

        i = 0
        dirmap = matrix.get_dirmap()
        accumulator = dirmap[direction]
        if direction in ('right', 'left'):
            i = y
        elif direction in ('down', 'up'):
            i = x

        while i != limit:
            matrix.inc_value()

            if direction in ('right', 'left'):
                matrix.setxy_to_value(x, i, matrix.get_value())
                y = i

            elif direction in ('down', 'up'):
                matrix.setxy_to_value(i, y, matrix.get_value())
                x = i

            i += accumulator

        print(f"After turning {direction}: x={x}, y={y}")
        print(f"my matrix state is currently: matrix value={matrix.get_value()}")
        return x, y

    if not isinstance(n, int):
        return []
    if n < 0:
        return []

    spiral = Matrix(n)
    left_limit, right_limit = -1, n
    top_limit, bottom_limit = 0, n
    x_ord, y_ord = 0, 0
    print(f"my matrix state is currently: {spiral.get_matrix()}")

    while spiral.get_value() < n*n:
        x_ord, y_ord = traverse_spiral(spiral, x_ord, y_ord, 'right', right_limit)
        x_ord, y_ord = traverse_spiral(spiral, x_ord+1, y_ord, 'down', bottom_limit)
        x_ord, y_ord = traverse_spiral(spiral, x_ord, y_ord-1, 'left', left_limit)
        x_ord, y_ord = traverse_spiral(spiral, x_ord-1, y_ord, 'up', top_limit)

        y_ord += 1
        right_limit -= 1
        bottom_limit -= 1
        left_limit += 1
        top_limit += 1

    return spiral.get_matrix()


#
# Make display better formatted
def display(m):
    if len(m) > 0:
        n = len(m[0])
        element_len = len(str(n * n))
        for i in range(n):
            for j in range(n):
                print(f"{m[i][j]:>{element_len}}", end=" ")
                if j == (n-1):
                    print()


def main():
    display(create_spiral(5))


if __name__ == '__main__':
    main()
