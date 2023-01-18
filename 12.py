# Write a function that gets two matrices of equal size. In cells of the same matrix of the same size, write larger
# elements than the corresponding cells of the first two matrices. For example, if the second cell of the third row
# of the first matrix contains the number 89, and the cell with the same pointer to the second matrix contains the
# number 10, then the number 89 must be written in the same cell of the third. The function must return the third matrix.

def func(f_matrix: list, s_matrix: list) -> list:
    r_matrix = s_matrix.copy()
    for i in range(len(f_matrix)):
        for j in range(len(f_matrix)):
            r_matrix[i][j] = f_matrix[i][j] if f_matrix[i][j] > s_matrix[i][j] else s_matrix[i][j]
    return r_matrix

