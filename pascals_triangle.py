def create_matrix(rows, cols, value):
    """
    Create an n * n array in the form of n lists of size n and populate with initial value
    :param rows:
    :param cols:
    :param value:
    :return: matrix
    """
    matrix = []
    for i in range(0, rows):
        row = []
        for j in range(0, cols):
            row.append(value)
        matrix.append(row)

    return matrix


def display_matrix(matrix, rows, cols):
    for i in range(0, rows):
        for j in range(0, cols):
            print(f"{matrix[i][j]} ", end='')
        print()


def pascal_triangle_build(n):
    """
    Fill up to the nth row of matrix represented as a list of lists
    so that the results represent a form of Pascal's Triangle.
    Take into account that python list elements always start at a position of 0
    :param n:
    :return:
    """
    triangle = create_matrix(n, n, 0)   # Initialise matrix with 0's
    # Fill in triangle
    for i in range(0, n):
        for j in range(0, i+1):
            if j == 0:
                triangle[i][0] = 1      # Initialise first column with 1's
            else:
                triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
    # display_matrix(triangle, n, n)
    return triangle


def easyline(n):
    pascals_triangle = pascal_triangle_build(n+1)
    #
    # Calculate sum of the squares on row n of an n + 1 row Pascal's Triangle. The first row is numbered 0!
    #
    total = 0
    for i in range(0, n + 1):
        total = total + int(pascals_triangle[n][i]) ** 2

    return total


print(easyline(0))
print(easyline(1))
print(easyline(2))
print(easyline(3))
print(easyline(4))
print(easyline(5))
print(easyline(6))
print(easyline(7))
print(easyline(50))
