class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def backtrack(row, col, i):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False
            
            if board[row][col] != word[i]:
                return False
            
            if i==len(word)-1:
                return True

            temp = board[row][col]
            board[row][col] = "#"

            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            for dr, dc in directions:
                    if  backtrack(row+dr, col+dc, i+1):
                        return True
                
            board[row][col] = temp
            return False
        
        for r in range(rows):
            for c in range(cols):
                if backtrack(r,c,0):
                    return True
        return False