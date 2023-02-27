# Matrix Determinant Calculator

This project is a simple Python script that calculates the determinant of a matrix using two different methods: the Leibniz method and the Gauss-Elimination method.

## Usage

To use this script, simply run the `determinant.py` file in your terminal, passing the matrix as a command-line argument. The matrix should be entered in row-major order, with rows separated by semicolons and values separated by spaces. For example, to calculate the determinant of the matrix


$\begin{bmatrix} 
   1 & 2 & 3 \\
   4 & 5 & 6 \\
   7 & 8 & 9 \\
   \end{bmatrix}$

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


The script will output the determinant of the matrix using both the Leibniz method and the Gauss-Elimination method.

## Methodology

### Leibniz Method

The Leibniz method has a time complexity of **O(n!)**, where n is the number of rows in the matrix. This method involves computing the sum of all possible products of elements from different rows and columns, where the sign of each product is $sign = (-1)^i$ where i is the current row. Therefore, it can be computationally expensive for large matrices.

### Gauss-Elimination Method

The Gauss-Elimination method has a time complexity of **O(n^3)**, where n is the number of rows in the matrix. This method involves transforming the matrix into row-echelon form using elementary row operations and then computing the determinant as the product of the diagonal elements. This method is generally faster than the Leibniz method, especially for large matrices.
