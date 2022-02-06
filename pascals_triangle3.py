def display_matrix(matrix, rows, cols):
    for i in range(0, rows):
        for j in range(0, cols):
            print(f"{matrix[i][j]} ", end='')
        print()


def easyline(x):

    def pascal_triangle_build(n):
        """
        Fill up to the nth row of matrix represented as a list of lists
        so that the results represent a form of Pascal's Triangle.
        Mehod takes into account the fact python list elements always start at a position of 0
        :param n:
        :return: list of lists
        """
        # Initialise a pascal's triangle matrix with 0's
        triangle_matrix = []
        for i in range(0, n):
            row = [0] * n
            triangle_matrix.append(row)

        # Fill in matrix with expected values
        for i in range(0, n):
            for j in range(0, i + 1):
                if j == 0:
                    triangle_matrix[i][0] = 1  # Initialise first column with 1's
                else:
                    triangle_matrix[i][j] = triangle_matrix[i - 1][j - 1] + triangle_matrix[i - 1][j]

        return triangle_matrix

    pascals_triangle = pascal_triangle_build(x + 1)
    #
    # Calculate sum of the squares on row x of an x + 1 row Pascal's Triangle. The first row is numbered 0!
    #
    total = 0
    for col in range(0, x + 1):
        total = total + int(pascals_triangle[x][col]) ** 2

    return total


print(easyline(0))
print(easyline(1))
print(easyline(2))
print(easyline(3))
print(easyline(4))
print(easyline(5))
print(easyline(6))
print(easyline(7))
print(easyline(8))
print(easyline(50))
