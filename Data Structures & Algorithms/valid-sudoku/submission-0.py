class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=collections.defaultdict(set)
        cols=collections.defaultdict(set)
        boxes=collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                values=board[r][c]
                if values==".":
                    continue
                if (values in rows[r] or values in cols[c] or values in boxes[(r//3,c//3)]):
                    return False
                rows[r].add(values)
                cols[c].add(values)
                boxes[(r//3,c//3)].add(values)
        return True
        