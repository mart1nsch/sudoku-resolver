sudoku = [
    [None,    1, None,    4, None, None, None, None,    2],
    [None, None, None, None,    6,    9, None, None,    4],
    [   9, None, None, None, None, None,    6, None,    7],
    [None,    9,    1,    6, None, None, None, None,    5],
    [   5, None, None, None, None,    4, None,    3, None],
    [   3,    8, None,    2, None,    1, None, None, None],
    [   1,    2, None,    7,    9, None,    5, None, None],
    [   7,    3, None, None, None,    5, None,    4,    9],
    [   8, None, None, None, None, None, None,    2,    3],
]

def find_empty() -> tuple:
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            if sudoku[i][j] is None:
                return (i, j)

def position_is_valid(num:int, row:int, col:int) -> bool:
    
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
                if sudoku[i][j] == num:
                    return False
        return True

    def check_row(num:int, row:int) -> bool:
        for i in sudoku[row]:
            if i == num:
                return False
        return True

    def check_col(num:int, col:int) -> bool:
        for i in sudoku:
            if i[col] == num:
                return False
        return True

    return check_area(num, row, col) and check_row(num, row) and check_col(num, col)

def solve() -> bool:
    position_empty = find_empty()
    if not position_empty:
        return True
    
    row, col = position_empty

    for num in range(1, 10):
        if position_is_valid(num, row, col):
            sudoku[row][col] = num

            if solve():
                return True
            
            sudoku[row][col] = None
    
    return False

def main():
    solve()
    for i in sudoku:
        print(i)

if __name__ == '__main__':
    main()