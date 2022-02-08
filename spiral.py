
# ToDo: 1) Research to see if the up, down, right and left functions can be collapsed.
# ToDo: 2) See if we can create a matrix class that will have global representations for value, fillcount etc.
# ToDo: 3) See if x and y co-ordinates can be represented as a data class.


def spiral(n):

    def init_matrix(x):
        return [[0 for i in range(x)] for i in range(x)]

    def traverse_spiral(matrix, x, y, direction, limit, value, count):
        """
        :param matrix: 2D array
        :param x: starting row value
        :param y: starting column value
        :param direction: current direction of numeric clockwise spiral
        :param limit: value of row or col to not go past
        :param value: starting value to fill into a spiral cell
        :param count: counter for how many cells filled so far
        :return:
        """
        i = 0
        dirmap = {'right': 1, 'down': 1, 'left': -1, 'up': -1}
        accumulator = dirmap[direction]
        if direction in ('right', 'left'):
            i = y
        elif direction in ('down', 'up'):
            i = x

        while i != limit:
            if direction in ('right', 'left'):
                matrix[x][i] = value
                y = i

            elif direction in ('down', 'up'):
                matrix[i][y] = value
                x = i

            value += 1
            count += 1
            i = i + accumulator
        print(f"After {direction}: x={x}, y={y}")
        print(f"my matrix state is currently: {matrix} count={count}")
        return x, y, value, count

    x_ord, y_ord = 0, 0
    array = init_matrix(n)
    print(f"After init: x_ord={x_ord}, y_ord={y_ord}")
    print(f"my matrix state is currently: {array}")
    val = 1
    counter = 0
    left_limit, right_limit = -1, n
    top_limit, bottom_limit = 0, n

    while counter < n*n:
        x_ord, y_ord, val, counter = traverse_spiral(array, x_ord, y_ord, 'right', right_limit, val, counter)
        x_ord, y_ord, val, counter = traverse_spiral(array, x_ord+1, y_ord, 'down', bottom_limit, val, counter)
        x_ord, y_ord, val, counter = traverse_spiral(array, x_ord, y_ord-1, 'left', left_limit, val, counter)
        x_ord, y_ord, val, counter = traverse_spiral(array, x_ord-1, y_ord, 'up', top_limit, val, counter)

        y_ord += 1
        right_limit -= 1
        bottom_limit -= 1
        left_limit += 1
        top_limit += 1

    return array


#
# Make display better formatted
def display(matrix):
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
