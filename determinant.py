
def determinant_with_Leibniz(matrix):
    dim = len(matrix)
    if dim < 1:
        return 0
    if dim == 1: # if dimension of the matrix equal to 1,the determinant is the single element of the matrix
        return matrix[0][0]
    if dim == 2: # if dimension of the matrix equal to 2, the determinant is the result of the equation matrix[1][1] * matrix[0][0] - matrix[0][1] - matrix[1][0]
        return matrix[1][1] * matrix[0][0] - matrix[0][1] * matrix[1][0]
    sign = -1
    det = 0
    for i in range(dim):
        submatrix = [row[:i] + row[i+1:] for row in matrix[1:]]
        subdet = determinant_with_Leibniz(submatrix)
        det += matrix[0][i] * sign ** i * subdet
    return det

def determinant_with_Gauss_Jordan_elimination(matrix):
    dim = len(matrix)
    for i in range(dim):
        for j in range(i + 1,dim):
            if matrix[i][i] != 0:
                ratio = matrix[j][i] / matrix[i][i] # how many times is necessary to remove the pivot
                for k in range(i,dim):
                    matrix[j][k] -= matrix[i][k] * ratio
    det = 1
    for i in range(dim):
        det *= matrix[i][i]
    return round(det)

def interface():
    global n,matrix
    n = int(input("Please enter the dimension of the matrix\n"))
    print("Please enter the matrix")
    matrix = [[int(x) for x in input().split()] for j in range(n)]
    print("Choose your method to calculate the determinant:")
    print("1. Gauss–Jordan Elimination Method")
    print("2. Leibniz Method")
    print("3. Both Methods")
    method_selector = int(input())
    match method_selector:
        case 1:
            print("The determinant of the matrix is", determinant_with_Leibniz(matrix))
        case 2:
            print("The determinant of the matrix is", determinant_with_Gauss_Jordan_elimination(matrix))
        case 3:
            print("The determinant of the matrix is:")
            print("Using Gauss–Jordan Elimination", determinant_with_Gauss_Jordan_elimination(matrix))
            print("Using Leibniz Method",determinant_with_Leibniz(matrix))

if __name__ == "__main__":
    interface()
