class SolutionUsingArrayCounting:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_rows_and_columns():
            columns = [[0] * 10 for _ in range(10)]
            for row in board:
                rows = [0] * 10
                for col_index, val in enumerate(row):
                    if val == '.':
                        continue
                    val = int(val)
                    rows[val] += 1
                    columns[col_index][val] += 1
                    if columns[col_index][val] > 1 or rows[val] > 1:
                        return False
            return True


        def check_subbox(x, y):
            values = [0] * 10
            for row in range(3):
                for col in range(3):
                    value = board[y+row][x+col]
                    if value == '.':
                        continue
                    value = int(value)
                    values[value] += 1
            if max(values) > 1:
                return False
            return True
        
        for y in range(0, 9, 3):
            for x in range(0, 9, 3):
                if not check_subbox(x, y):
                    return False
        return check_rows_and_columns()


class SolutionUsing3HashSets:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == '.':
                    continue
                box_index = r // 3 + c // 3 * 3
                if value in rows[r] or value in cols[c] or value in boxes[box_index]:
                    return False
                rows[r].add(value)
                cols[c].add(value)
                boxes[box_index].add(value)
        return True


class SolutionUsingBitmasking:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == '.':
                    continue

                value = 1 << int(board[r][c])
                box_index = (r // 3) * 3 + (c // 3)

                if rows[r] & value or cols[c] & value or boxes[box_index] & value:
                    return False
                
                rows[r] |= value
                cols[c] |= value
                boxes[box_index] |= value
        return True


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return SolutionUsingBitmasking().isValidSudoku(board)


            
