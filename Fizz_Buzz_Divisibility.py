def divisibility():
    User_Number = int(input("Please Input What Number You'd Like to Use: "))
    if User_Number % 3 == 0 and User_Number % 5 == 0:
        print("FizzBuzz")
    elif User_Number % 5 == 0:
        print("Buzz")
    elif User_Number % 3 == 0:
        print("Fizz")
    else: 
        print("Hello World")

divisibility()