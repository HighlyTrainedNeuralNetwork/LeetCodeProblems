# Naive solution of checking all directions for all locations is too slow. Intended solution seems to be precomputing
# distances ala a "delta" array so that calculcation does not need to be repeated.

def orderOfLargestPlusSign(n, mines):
    matrix = [[n] * n for i in range(n)]
    for mine in mines:
        matrix[mine[0]][mine[1]] = 0
    for row in range(n):
        left = 0
        right = 0
        up = 0
        down = 0
        for col, reverse_col in zip(range(n), reversed(range(n))):
            left = left + 1 if matrix[row][col] != 0 else 0
            matrix[row][col] = min(matrix[row][col], left)
            right = right + 1 if matrix[row][reverse_col] != 0 else 0
            matrix[row][reverse_col] = min(matrix[row][reverse_col], right)
            up = up + 1 if matrix[col][row] != 0 else 0
            matrix[col][row] = min(matrix[col][row], up)
            down = down + 1 if matrix[reverse_col][row] != 0 else 0
            matrix[reverse_col][row] = min(matrix[reverse_col][row], down)
    return max(max(matrix, key=max))

n = 5
mines = [[4,2]]
print(orderOfLargestPlusSign(n, mines))