def solveSudoku(board):
    def solve(board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    boxVals = [board[3 * (row // 3) + i][3 * (col // 3) + j] for i in range(3) for j in range(3)]
                    colVals = [board[i][col] for i in range(9)]
                    vals = set([int(val) for val in boxVals + colVals + board[row] if val != "."])
                    candidates = list(set(range(1, 10)) - vals)
                    for candidate in candidates:
                        board[row][col] = str(candidate)
                        if solve(board):
                            return True
                        board[row][col] = "."
                    return False
        return True
    solve(board)

if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]
    output = solveSudoku(board)
    print(output, board)
