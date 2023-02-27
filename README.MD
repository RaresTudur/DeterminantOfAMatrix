# Matrix Determinant Calculator

This project is a simple Python script that calculates the determinant of a matrix using two different methods: the Leibniz method and the Gauss-Elimination method.

## Usage

To use this script, simply run the `determinant.py` file in your terminal, passing the matrix as a command-line argument. The matrix should be entered in row-major order, with rows separated by semicolons and values separated by spaces. For example, to calculate the determinant of the matrix

$$ \begin{bmatrix} 
   1 & 2 & 3 \\
   4 & 5 & 6 \\
   7 & 8 & 9 \\
   \end{bmatrix}
$$
you would run the following command:

```
python3 determinant.py
Please enter the dimension of the matrix:
3
Please enter the matrix:
1 2 3
4 5 6
7 8 9
Choose your method to calculate the determinant:
1. Gauss Elimination Method
2. Leibniz Method
3. Both Methods
```