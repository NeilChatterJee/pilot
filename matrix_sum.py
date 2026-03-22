matrix = [[6, 8],
          [4, 1],
          [5, 7]]
for i in range(3):
    row_total = 0
    for j in range(2):
        row_total += matrix[i][j]
    print(row_total)