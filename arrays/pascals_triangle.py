
def pascals_triangle(numRows):
    pt = []

    for i in range(numRows):
        row = []
        for j in range(i + 1):
            print(row)
            if j == 0 or j == i:
                row.append(1)
        pt.append(row)
    return pt
op = pascals_triangle(5)
print(op)
