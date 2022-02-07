import sys
# ToDo: 1) remove the need to adjust x and y return values before returning them
# ToDo: 2) Research to see if the up, down, right and left functions can be collapsed.
# ToDo: 3) See if we can create a matrix class that will have global representations for value and count


def spiral(n):

    def init_matrix(x):
        return [[0 for i in range(x)] for i in range(x)]

    def right(matrix, x, y, limit, value, count):
        while y <= limit:
            if matrix[x][y] == 0:
                matrix[x][y] = value
                value += 1
                count += 1
                # print(f"x={x}, y={y}, limit={limit}")
                # print(f"my matrix state is currently: {matrix}")
            y += 1
        return x, y-1, value, count

    def left(matrix, x, y, limit, value, count):
        while y >= limit:
            if matrix[x][y] == 0:
                matrix[x][y] = value
                value += 1
                count += 1
            y -= 1
        return x, y+1, value, count

    def down(matrix, x, y, limit, value, count):
        while x <= limit:
            if matrix[x][y] == 0:
                matrix[x][y] = value
                value += 1
                count += 1
            x += 1
        return x-1, y, value, count

    def up(matrix, x, y, limit, value, count):
        while x >= limit:
            if matrix[x][y] == 0:
                matrix[x][y] = value
                value += 1
                count += 1
            x -= 1
        return x+1, y, value, count

    x_ord, y_ord = 0, 0
    array = init_matrix(n)
    print(f"After init: x_ord={x_ord}, y_ord={y_ord}")
    print(f"my matrix state is currently: {array}")
    all_filled = False
    val = 1
    fillcount = 0
    left_limit, right_limit = 0, n - 1
    top_limit, bottom_limit = 0, n - 1

    while not all_filled:
        x_ord, y_ord, val, fillcount = right(array, x_ord, y_ord, right_limit, val, fillcount)
        print(f"After right: x_ord={x_ord}, y_ord={y_ord}")
        print(f"my matrix state is currently: {array}")
        # sys.exit(0)
        x_ord, y_ord, val, fillcount = down(array, x_ord, y_ord, bottom_limit, val, fillcount)
        print(f"After down: x_ord={x_ord}, y_ord={y_ord}")
        print(f"my matrix state is currently: {array}")
        x_ord, y_ord, val, fillcount = left(array, x_ord, y_ord, left_limit, val, fillcount)
        print(f"After down: x_ord={x_ord}, y_ord={y_ord}")
        print(f"my matrix state is currently: {array}")
        x_ord, y_ord, val, fillcount = up(array, x_ord, y_ord, top_limit, val, fillcount)
        print(f"After up: x_ord={x_ord}, y_ord={y_ord}")
        print(f"my matrix state is currently: {array}")
        # sys.exit(0)

        x_ord += 1
        y_ord += 1
        right_limit -= 1
        bottom_limit -= 1
        left_limit += 1
        top_limit += 1
        if fillcount == n * n:
            all_filled = True

    return array


#
# Make display better formatted
def display(matrix):
    n = len(matrix[0])
    element_len = len(str(n * n))
    for i in range(n):
        for j in range(n):
            print(f"{matrix[i][j]:>{element_len}}", end=" ")
            if j == (n-1):
                print()


spiral_matrix = spiral(5)
display(spiral_matrix)
# sys.exit(0)
spiral_matrix = spiral(1)
display(spiral_matrix)
