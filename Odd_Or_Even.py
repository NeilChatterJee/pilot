def Two_Digit_Number():
    integer = int(input("Please Input Any Integer: "))
    if integer < 10:
        print("This is a 1 digit number! ")
    elif integer > 9 and integer < 100:
        print("This is a two digit number!")
    elif integer > 99 and integer < 1000:
        print("This is a 3 digit number! ")

def Odd_Or_Even():
    number = int(input("Please Input A Number: "))
    if number % 2 == 0:
        print("This An Even Number: ")
    else:
        print("This Number Is Odd")

Two_Digit_Number()
Odd_Or_Even()
