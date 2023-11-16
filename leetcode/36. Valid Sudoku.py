class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Function to check if there are no repeated elements in each column
        def check_column(board):
            for i in range(9):
                column = []
                for j in range(9):
                    column.append(board[j][i])
                # Filter out "." and create a list of valid values in the column
                column = [x for x in column if x != "."]
                # Check for duplicates in the column
                if len(set(column)) != len(column):
                    return False
            return True

        # Function to check if there are no repeated elements in each row
        def check_row(board):
            for i in range(9):
                row = [x for x in board[i] if x != "."]
                # Check for duplicates in the row
                if len(set(row)) != len(row):
                    return False
            return True

        # Function to check if the entire Sudoku board is valid
        def is_valid_sudoku(board):
            # Function to check if a unit (row, column, or submatrix) is valid
            def is_valid_unit(unit):
                unit = [i for i in unit if i != '.']
                return len(unit) == len(set(unit))

            for i in range(9):
                # Check rows and columns
                if not (is_valid_unit(board[i]) and is_valid_unit([board[j][i] for j in range(9)])):
                    return False

                # Check 3x3 submatrices
                row, col = divmod(i, 3)
                submatrix = [board[x][y] for x in range(row * 3, (row + 1) * 3) for y in range(col * 3, (col + 1) * 3)]
                if not is_valid_unit(submatrix):
                    return False

            return True

        # Check if the Sudoku board is valid by calling the three functions
        if check_column(board) and check_row(board) and is_valid_sudoku(board):
            return True
        return False
