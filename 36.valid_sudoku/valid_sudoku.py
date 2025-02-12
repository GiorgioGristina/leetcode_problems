from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        col = defaultdict(set)
        row = defaultdict(set)
        square = defaultdict(set)
        # print(board[0][1])
        for ir, r in enumerate(board):
            for ic, c in enumerate(r):
                if c == ".":
                    continue
                print(f"row {ir} col {ic} val is: {c}")
                # check col 
                if c in col[ic]:
                    return False
                else: 
                    col[ic].add(c)
                
                # check row  
                if c in row[ir]:
                    return False
                else: 
                    row[ir].add(c)
                
                 # check square
                if c in square[str(ir//3) + str(ic // 3)]:
                    return False
                else: 
                    square[str(ir//3) + str(ic // 3)].add(c)

        return True


solution = Solution()

#         Input: 
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
# Output: true
print(f"It is a valid sudoku: {solution.isValidSudoku(board)}")


# Input: 
board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
# Output: false

print(f"It is a valid sudoku: {solution.isValidSudoku(board)}")
