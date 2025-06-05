# Approach 1
# Issue: We set row/cols upfront, which affects already existing 0's in
# other rows/cols
# Works for [[1,1,1], [1,0,1], [1,1,1]]
# Doesn't work for [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]

def set_matrixrix_zero_2 (matrix):
    row_set = {}
    col_set = {}

    for row in range(len(matrix)):
        if row not in row_set:
            for col in range(len(matrix[0])):
                if col not in col_set:
                    if (matrix[row][col] == 0):
                        row_set[row] = True
                        col_set[col] = True

                        # Set Col values to zero
                        for i in range(len(matrix)):
                            matrix[i][col] = 0

            if row in row_set:
                # Set Row values to zero
                for j in range(len(matrix[0])):
                    matrix[row][j] = 0
    return matrix

# Approach 2
# First find out all the rows/cols where 0's exist, then set those rows/cols to 0s
def set_matrixrix_zero (matrix):
    row_set = {}
    col_set = {}

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                row_set[row] = True
                col_set[col] = True


    print(row_set, col_set)

    # Set Rows to 0
    for row in row_set.keys():
        for col in range(len(matrix[0])):
            matrix[row][col] = 0

    # Set cols to 0
    for col in col_set.keys():
        for row in range(len(matrix)):
            matrix[row][col] = 0

    return matrix

matrix = [[1,1,1], [1,0,1], [1,1,1]]
matrix = [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
op = set_matrixrix_zero(matrix)
print(op)
