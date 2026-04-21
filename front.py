import streamlit as st
import numpy as np
from algorithm import SudokuResolver

sudoku = np.zeros(81, dtype=np.int16).reshape((9, 9))

st.title('Sudoku Resolver')
st.text('Enter your sudoku (0 means No Number)')

sudoku_edited = st.data_editor(sudoku, num_rows=9)

if st.button('Resolve Sudoku'):
    error = False
    at_least_one_number = False

    for i in sudoku_edited:
        for j in i:
            if j not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                error = True
                break
            if j != 0:
                at_least_one_number = True
        if error:
            break
    
    if not at_least_one_number:
        error = True

    if not error:
        sudoku_resolver = SudokuResolver(sudoku_edited)
        sudoku_resolver.solve()
        st.text('Solution')
        st.dataframe(sudoku_resolver.get_sudoku())
    else:
        st.text('Please, enter a valid Sudoku!')