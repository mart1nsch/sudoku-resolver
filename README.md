# Sudoku Resolver
#### Video Demo:  https://youtu.be/nFDd5Xc6cHU
#### Description:
This is an application made with Streamlit and Python to Solve Sudokus!
Before you use it, you need to run these commands below

    py -3.13 -m venv venv
    ./venv/Scripts/Activate.ps1
    pip install requirements.txt
    streamlit run front.py

After this, you're good to go!

To use it, you just need to enter a valid sudoku inside the table displayed and press the "Resolve Sudoku" button below the table!

## Logic Information
For the Front-End of this application I used Streamlit, witch you can find the source code inside the front.py archive.

For the Back-End, I used enterilly Python, with a Class named SudokuResolver. You can find the source code inside algorithm.py archive.

To implement this algorithm, I had to use recursion, so, if the logic had choosen the wrong path, it could backwards and return to a point where it could take another path. This goes for a while, until it finds a solution or doesn't have any other path to take.