number_of_inputs = int(input("How Many Numbers Would You Like To Input ? : "))
smallest_number = 10
largest_number = 11
for i in range(0, number_of_inputs):
    input("Please Input A Number: ")
    if i < smallest_number:
        smallest_number = i
    elif i > largest_number:
        largest_number = i

print(smallest_number)
print(largest_number)