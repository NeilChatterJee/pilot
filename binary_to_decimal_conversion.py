binary_input = input("Enter Any Binary Number: ")
def for_loop_binary_converter(inputs):
    exponent = 0
    converted_number = 0
    reverse_binary_number = inputs[::-1]
    for num in reverse_binary_number:
        if num == "1" or num == "0":
            converted_number = converted_number + (int(num) * (2 ** exponent))
            exponent += 1
        elif num != "1" or num != "0":
            continue
    print(f"Your Converted Number is {converted_number}")



def while_loop_binary_converter(inputs1):
    d = 0
    exponent = 0
    converted_number = 0
    reverse_binary_user_input = inputs1[::-1]
    while d < len(reverse_binary_user_input):
        num = reverse_binary_user_input[d]
        if num == "1" or num == "0":
            converted_number = converted_number + (int(num) * (2 ** exponent))
            exponent += 1
        elif num != "1" or num != "0":
            continue
        d += 1
    print(f"Your Converted Decimal Number is {converted_number}")

while_loop_binary_converter(binary_input)

