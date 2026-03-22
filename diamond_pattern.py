rows = 5 

for i in range(1, rows+1): 

    # creating the pattern for spaces 

    for k in range(rows-i): 

        print(' ', end='') 

         

    # creating pattern for numbers 

    for j in range(1, i+1): 

        print(i, end=' ') 

    # moves the cursor to the next line 

    print()



for i in range(rows - 1, 0, -1):
    for k in range(rows - i):
        print(' ', end = '') 
    for j in range(i):
        print(i, end = ' ')
    print()