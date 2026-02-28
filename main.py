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

def create_reversed_sudoku(sudoku:list) -> list[list]:
    reversed_sudoku = []

    for i in range(len(sudoku)):
        line = []
        for j in range(len(sudoku[i])):
            line.append(sudoku[j][i])
        reversed_sudoku.append(line)
    
    return reversed_sudoku

def return_missing_values_from_line_or_row(line_or_row:list) -> list:
    missing_values = []

    for i in range(1, 10):
        if not i in line_or_row:
            missing_values.append(i)
    
    return missing_values

def get_missing_values(matrix:list) -> list:
    missing_values = []
    for i in matrix:
        missing_values.append(return_missing_values_from_line_or_row(i))
    return missing_values

reversed_sudoku = create_reversed_sudoku(sudoku)

lines_missing_values = get_missing_values(sudoku) 
rows_missing_values = get_missing_values(reversed_sudoku)