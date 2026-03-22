rows = 7
for i in range(rows, 0, -1):
    for k in range(rows - i):
        print(' ', end = '') 
    for j in range(i -2):
        print(i, end = ' ')
        
    print()