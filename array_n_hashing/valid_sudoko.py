
def isValidSudoku(board) -> bool:
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for r in range(9):
        for c in range(9):
            val = board[r][c]

            if val == ".":
                continue

            # box index
            box_index = (r//3) * 3 + (c//3)

            if (val in rows[r] or val in cols[c] or val in boxes[box_index]):
                return False
            
            rows[r].add(val)
            cols[c].add(val)
            boxes[box_index].add(val)

    return True




board = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]


print(isValidSudoku(board))