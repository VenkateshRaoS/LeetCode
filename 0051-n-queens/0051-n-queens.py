class Solution:
    def solveNQueens(self, n):
        result = []
        board = ["." * n for _ in range(n)]

        cols = set()
        diag1 = set()
        diag2 = set()

        def backtrack(r):
            if r == n:
                result.append(board[:])
                return
            
            for c in range(n):
                if c in cols or (r - c) in diag1 or (r + c) in diag2:
                    continue
                
                # place queen
                cols.add(c)
                diag1.add(r - c)
                diag2.add(r + c)
                board[r] = board[r][:c] + "Q" + board[r][c+1:]

                backtrack(r + 1)

                # remove queen
                cols.remove(c)
                diag1.remove(r - c)
                diag2.remove(r + c)
                board[r] = board[r][:c] + "." + board[r][c+1:]

        backtrack(0)
        return result