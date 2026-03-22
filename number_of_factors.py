user_input = int(input("Please Enter A Number: "))
count_of_factors = 0
for i in range(1, user_input + 1):
    if user_input % i == 0:
        count_of_factors += 1
print(count_of_factors)