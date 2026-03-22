user_input = input("Enter Any Number: ")
n = int(user_input)
k = n + 4
for i in range(1, n + 1, 1):
    for j in range(1, i + 1):
        print(" " * k, i, end = " ")
        k -= 1
    print()   