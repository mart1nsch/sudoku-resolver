class SudokuResolver:
    sudoku = []

    def __init__(self, new_sudoku):
        self.sudoku = new_sudoku
    
    def get_sudoku(self):
        return self.sudoku

    def find_empty(self) -> tuple:
        for i in range(len(self.sudoku)):
            for j in range(len(self.sudoku[i])):
                if self.sudoku[i][j] == 0:
                    return (i, j)

    def position_is_valid(self, num:int, row:int, col:int) -> bool:
        
        def check_area(num:int, row:int, col:int) -> bool:
            groups_of_numbers = {
                0: [0, 1, 2],
                1: [0, 1, 2],
                2: [0, 1, 2],
                3: [3, 4, 5],
                4: [3, 4, 5],
                5: [3, 4, 5],
                6: [6, 7, 8],
                7: [6, 7, 8],
                8: [6, 7, 8]
            }

            for i in groups_of_numbers[row]:
                for j in groups_of_numbers[col]:
                    if self.sudoku[i][j] == num:
                        return False
            return True

        def check_row(num:int, row:int) -> bool:
            for i in self.sudoku[row]:
                if i == num:
                    return False
            return True

        def check_col(num:int, col:int) -> bool:
            for i in self.sudoku:
                if i[col] == num:
                    return False
            return True

        return check_area(num, row, col) and check_row(num, row) and check_col(num, col)

    def solve(self) -> bool:
        position_empty = self.find_empty()
        if not position_empty:
            return True
        
        row, col = position_empty

        for num in range(1, 10):
            if self.position_is_valid(num, row, col):
                self.sudoku[row][col] = num

                if self.solve():
                    return True
                
                self.sudoku[row][col] = 0
        
        return False