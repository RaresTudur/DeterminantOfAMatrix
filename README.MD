# Matrix Determinant Calculator
This project is a simple Python script that calculates the determinant of a matrix using two different methods: the Leibniz method and the Gauss–Jordan elimination.
## Usage
To use this script, simply run the `determinant.py` file in your terminal, passing the matrix as a command line argument. The array must be entered in major row order, with rows separated by semicolons and values separated by spaces. For example, to calculate the determinant of the matrix:

```math
\begin{matrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9 \\
\end{matrix}
```
you should execute the following command:

```python
python3 determinant.py
Please enter the size of the matrix:
3
Please enter the matrix:
1 2 3
4 5 6
7 8 9
Choose the method of calculating the determinant:
1. Gauss–Jordan Elimination Method
2. Leibniz method
3. Both methods
```
## Techniques
### Leibniz method
The Leibniz method has a time complexity of **O(n!)**, where n is the number of rows in the matrix. This method involves calculating the sum of all possible products of elements in different rows and columns, where the sign of each product is $sign = (-1)^i$ where i is the current row. Therefore, this method can be computationally expensive for large matrices.
### Gauss–Jordan elimination method

The Gauss–Jordan elimination method has a time complexity of **O(n^3)**, where n is the number of rows in the matrix. This method involves transforming the matrix into row echelon form using elementary row operations and then computing the determinant as the product of the diagonal elements. This method is generally faster than the Leibniz method, especially for large matrices.

## Created by
-- Tudur Rares, Grupa 142
