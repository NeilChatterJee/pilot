user_input = input("Enter Any Number: ")
n = int(user_input)
for i in range(0, n, 1):
    for j in range(1, i + 2):
        print(j, end= " ")
    print()   


