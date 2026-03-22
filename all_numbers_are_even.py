is_even = True
for i in range(5):
    x = int(input("Enter a Number: "))
    if x % 2 != 0:
        is_even = False

if is_even:
    print("All Numbers Even!")
elif is_even == False:
    print("All Numbers Not Even!")


