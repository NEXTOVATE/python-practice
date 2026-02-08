# :Given a matrix (list of lists), write code to compute:
# Matrix transpose
# Maximum of each row
# Minimum of each column
# Sum of both diagonals
# Note: Do not use NumPy. Do not create extra matrices except for final outputs.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Matrix transpose
transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
print("Matrix Transpose:")
for row in transpose:
    print(row)
# Maximum of each row
max_of_rows = [max(row) for row in matrix]
print("Maximum of each row:", max_of_rows)
# Minimum of each column
min_of_columns = [min(matrix[i][j] for i in range(len(matrix))) for j in range(len(matrix[0]))]
print("Minimum of each column:", min_of_columns)
# Sum of both diagonals
primary_diagonal_sum = sum(matrix[i][i] for i in range(len(matrix)))
secondary_diagonal_sum = sum(matrix[i][len(matrix) - 1 - i] for i in range(len(matrix)))
total_diagonal_sum = primary_diagonal_sum + secondary_diagonal_sum
print("Sum of both diagonals:", total_diagonal_sum) 
