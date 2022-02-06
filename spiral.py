import sys
# ToDo: 1) remove the need to adjust x and y return values before returning them
# ToDo: 2) Eliminate the need for the global: value
# ToDo: 3) Eliminate the need for the global: fill_count
# ToDo: 4) Have the matrix display function display numbers in a well formatted fashion
# ToDo: 5) Research to see if the up, down, right and left functions can be collapsed.

def spiral(n):
    global value
    global fill_count
    value = 1
    fill_count = 0

    def init_matrix(n):
        matrix = [[0 for i in range(n)] for i in range(n)]

        return matrix

        # matrix.append([0])
        # matrix[0].extend([0] * (n-1))
        # matrix.extend([matrix[0]] * (n-1))

    def right(matrix, x, y, limit):
        global value
        global fill_count
        while y <= limit:
            if matrix[x][y] == 0:
                matrix[x][y] = value
                value += 1
                fill_count += 1
                #print(f"x={x}, y={y}, limit={limit}")
                #print(f"my matrix state is currently: {matrix}")
            y += 1
        return x, y-1

    def left(matrix, x, y, limit):
        global value
        global fill_count
        while y >= limit:
            if matrix[x][y] == 0:
                matrix[x][y] = value
                value += 1
                fill_count += 1
            y -= 1
        return x, y+1

    def down(matrix, x, y, limit):
        global value
        global fill_count
        while x <= limit:
            if matrix[x][y] == 0:
                matrix[x][y] = value
                value += 1
                fill_count += 1
            x += 1
        return x-1, y

    def up(matrix, x, y, limit):
        global value
        global fill_count
        while x >= limit:
            if matrix[x][y] == 0:
                matrix[x][y] = value
                value += 1
                fill_count += 1
            x -= 1
        return x+1, y


    x = 0
    y = 0
    matrix = init_matrix(n)
    print(f"After init: x={x}, y={y}")
    print(f"my matrix state is currently: {matrix}")
    all_filled = False
    x = 0
    y = 0
    right_limit = n - 1
    left_limit = 0
    bottom_limit = n - 1
    top_limit = 0

    while not all_filled:
        x, y = right(matrix, x, y, right_limit)
        print(f"After right: x={x}, y={y}")
        print(f"my matrix state is currently: {matrix}")
        # sys.exit(0)
        x, y = down(matrix, x, y, bottom_limit)
        print(f"After down: x={x}, y={y}")
        print(f"my matrix state is currently: {matrix}")
        x, y = left(matrix, x, y, left_limit)
        print(f"After down: x={x}, y={y}")
        print(f"my matrix state is currently: {matrix}")
        x, y = up(matrix, x, y, top_limit)
        print(f"After up: x={x}, y={y}")
        print(f"my matrix state is currently: {matrix}")
        #sys.exit(0)

        x += 1
        y += 1
        right_limit -= 1
        bottom_limit -= 1
        left_limit += 1
        top_limit += 1
        if fill_count == n * n:
            all_filled = True

    return matrix

#
# Make display better formatted
def display(matrix):
    n = len(matrix)
    for i in range(n):
        print(matrix[i])


spiral_matrix = spiral(2)
display(spiral_matrix)
spiral_matrix = spiral(1)
display(spiral_matrix)