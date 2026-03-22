import random
list_val = []
for i in range(10,51):
    list_val.append(i)

matrix = []

for f in range(3):
    for j in range(4):
        rand_1 = random.choice(list_val)
        rand_2 = random.choice(list_val)
        rand_3 = random.choice(list_val)
        rand_4 = random.choice(list_val)
        matrix_inner_list = [rand_1, rand_2, rand_3, rand_4]
    matrix.append(matrix_inner_list)

l = 0
for val in matrix:
    print(matrix[l])
    l += 1

matrix_value_sum = 0
for v in matrix:
    for k in v:
        matrix_value_sum += k

print(f"Matrix Sum: {matrix_value_sum}")

row_number = 1
for row in matrix:
    row_sum = 0
    for value in row:
        row_sum += value
    print(f"Row {row_number} Sum: {row_sum}")
    row_number += 1

diagonal_sum = 0
j = 0
##### Matrix Diagonals
for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                diagonal_sum += matrix[i][j]

print(diagonal_sum)





count_of_rows = len(matrix)
count_of_columns = len(matrix[0])
#### Sum of Columns
for j in range(count_of_columns):
    column_sum = 0
    for i in range(count_of_rows):
        column_sum += matrix[i][j]
    print(column_sum)