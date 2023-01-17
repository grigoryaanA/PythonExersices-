#Write a function that will generate a matrix whose elements are '*',
#change the elements of the diagonal of the matrix, '#' symbol.

def generate_matrix(n):
    part = ['*'] * n
    matrix= []
    for i in range(n):
        matrix.append(part.copy())

    for i in range(n):
        for j in range(n):
            if i == j:
                matrix[i][j] = '#'

    return matrix
