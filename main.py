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

def found_position_to_place(number:int, row:int = None, col:int = None) -> tuple:
    if row is not None:
        for i in range(len(sudoku[row])):
            if sudoku[row][i] is None:
                return (row, i)

def place_number(number:int, position:tuple):
    sudoku[position[0]][position[1]] = number

def remove_missing_value(number:int, missing_list:list):
    pass

def place_missing_values(missing:tuple, reversed_sudoku:list[list]):
    for i in range(1, 10):
        for row in range(len(missing[0])):
            if i in missing[0][row]:
                place_number(i, found_position_to_place(number=i, row=row))
                remove_missing_value(i, missing[0][row])


def main():
    reversed_sudoku = create_reversed_sudoku(sudoku)
    missing_values = (get_missing_values(sudoku), get_missing_values(reversed_sudoku))
    place_missing_values(missing_values, reversed_sudoku)
    
    for i in sudoku:
        print(i)

main()