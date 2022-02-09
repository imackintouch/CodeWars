# ToDo: 1) See if x and y co-ordinates can be represented as a data class.
# ToDo: 2) Create setter functions that are easy to increment


def spiral(n):
    class Matrix:

        def __init__(self, size):
            self.size = size
            self.value = 0
            self.filled_count = 0
            self.matrix = self.init_matrix(size)
            self.dirmap = {'right': 1, 'down': 1, 'left': -1, 'up': -1}

        def init_matrix(self, x):
            return [[0 for i in range(x)] for i in range(x)]

        def get_matrix(self):
            return self.matrix

        def get_filled_count(self):
            return self.filled_count

        def get_value(self):
            return self.value

        def get_dirmap(self):
            return self.dirmap

        def set_filled_count(self, count):
            self.filled_count = count

        def inc_filled_count(self, inc=1):
            self.filled_count += inc

        def set_value(self, value):
            self.value = value

        def inc_value(self, inc=1):
            self.value += inc

    def traverse_spiral(matrix_obj, x, y, direction, limit):
        """
        :param matrix_obj: Matrix object to process
        :param x: starting row
        :param y: starting col
        :param direction: Direction to start filling
        :param limit: row or column value to mark the limit of current fill.
        :return: the x,y location of the last fill.
        """

        i = 0
        dirmap = matrix_obj.get_dirmap()
        accumulator = dirmap[direction]
        if direction in ('right', 'left'):
            i = y
        elif direction in ('down', 'up'):
            i = x

        while i != limit:
            matrix_obj.inc_value()

            if direction in ('right', 'left'):
                matrix_obj.matrix[x][i] = matrix_obj.get_value()
                y = i

            elif direction in ('down', 'up'):
                matrix_obj.matrix[i][y] = matrix_obj.get_value()
                x = i

            matrix_obj.inc_filled_count()
            i = i + accumulator

        print(f"After turning {direction}: x={x}, y={y}")
        print(f"my matrix state is currently: matrix count={matrix_obj.get_filled_count()}")
        return x, y

    x_ord, y_ord = 0, 0
    array = Matrix(n)
    print(f"After init: x_ord={x_ord}, y_ord={y_ord}")
    print(f"my matrix state is currently: {array.get_matrix()}")
    left_limit, right_limit = -1, n
    top_limit, bottom_limit = 0, n

    while array.get_filled_count() < n*n:
        x_ord, y_ord = traverse_spiral(array, x_ord, y_ord, 'right', right_limit)
        x_ord, y_ord = traverse_spiral(array, x_ord+1, y_ord, 'down', bottom_limit)
        x_ord, y_ord = traverse_spiral(array, x_ord, y_ord-1, 'left', left_limit)
        x_ord, y_ord = traverse_spiral(array, x_ord-1, y_ord, 'up', top_limit)

        y_ord += 1
        right_limit -= 1
        bottom_limit -= 1
        left_limit += 1
        top_limit += 1

    return array


#
# Make display better formatted
def display(m):
    matrix = m.get_matrix()
    if len(matrix) > 0:
        n = len(matrix[0])
        element_len = len(str(n * n))
        for i in range(n):
            for j in range(n):
                print(f"{matrix[i][j]:>{element_len}}", end=" ")
                if j == (n-1):
                    print()


def main():
    spiral_matrix = spiral(5)
    display(spiral_matrix)


if __name__ == '__main__':
    main()
