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
#### Archive front.py

That's the Front-End and core of the application. I used Streamlit to create a nice application. I choose that library because it's easy to use and you can create an app really fast with it.

For this project, i've used these methods:

1. title: To show the title of the application really big.
2. text: I used it to show important information for the user, like where to put their sudoku, and where is the solution or information about an error.
3. button: So the user can actually do a thing. The application only have one button, witch function is to submit the sudoku to the algorithm and show the solution to the user.
4. data_editor: For the table that the user can type their sudoku.
5. dataframe: Table that shows the solution of the sudoku. It only appears to the user when he clicks the "Resolve Sudoku" button.

#### Archive algorithm.py

That's the Back-End and the algorithm that solves the sudoku. I created a class named SudokuResolver with methods to solve the problem. Below, there's a explanation about every method inside this class.

1. __init__: It's the method that creates an object of these class. It expects to receive the sudoku that the user entered in the Front-End, and define it to the attribute named sudoku.
2. get_sudoku: It only return the attribut sudoku. It's used to show the solved sudoku to the user in the Front-End.
3. find_empty: Function that process every position of the sudoku looking for a position that is 0, witch is a position that doesn't have a number yet. It returns the empty matrix position to fill it.
4. position_is_valid: This function has the objective to verify if the number that the algorithm put in an empty position is valid. For example, if you have the number 2 already in the first column, you can't put the number 2 elsewhere in the first column. So, this function is to prevent this type of problems. It returns True if is valid, or False if is not.
5. solve: It's the main function of this class. It starts the recursion putting a value in every empty position, until the sudoku it's solved or doesn't have a solution to it. It returns True if the sudoku it's solved, or False if it's not the case.

## Inspiration Idea
I had this project idea while I was playing sudoku in a book, for a second, I talked to me and surprised myself because no one plays sudoku in a book nowadays. If people play it, they play in their phone or elsewhere, like a computer.

After that, I imagened that creating a sudoku resolver would be a different project and outside the usual Front-End application made with HTML, CSS and JavaScript.

I was liking Python and I started this journey. It was really difficult in the start, because my algorithm didn't want to work properly. So, I had to search a lot on how to implement a good algorithm to solve it. I liked a lot to do this and now i don't need to see sudoku's answers online again, i can just ask to my application!