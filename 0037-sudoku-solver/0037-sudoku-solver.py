class Solution:
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []

        # Initialize sets and empty cells
        for r in range(9):
            for c in range(9):
                ch = board[r][c]
                if ch == '.':
                    empties.append((r, c))
                else:
                    rows[r].add(ch)
                    cols[c].add(ch)
                    boxes[(r // 3) * 3 + (c // 3)].add(ch)

        def backtrack():
            if not empties:
                return True

            # Pick the empty cell with the fewest candidates
            best_idx = -1
            best_candidates = None

            for i, (r, c) in enumerate(empties):
                b = (r // 3) * 3 + (c // 3)
                candidates = [ch for ch in '123456789'
                              if ch not in rows[r]
                              and ch not in cols[c]
                              and ch not in boxes[b]]

                if not candidates:
                    return False

                if best_candidates is None or len(candidates) < len(best_candidates):
                    best_candidates = candidates
                    best_idx = i
                    if len(best_candidates) == 1:
                        break

            r, c = empties.pop(best_idx)
            b = (r // 3) * 3 + (c // 3)

            for ch in best_candidates:
                board[r][c] = ch
                rows[r].add(ch)
                cols[c].add(ch)
                boxes[b].add(ch)

                if backtrack():
                    return True

                board[r][c] = '.'
                rows[r].remove(ch)
                cols[c].remove(ch)
                boxes[b].remove(ch)

            empties.insert(best_idx, (r, c))
            return False

        backtrack()