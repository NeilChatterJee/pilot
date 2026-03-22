def total(n): 

    if n == 1: 

        return 1 

    return n * total(n-1) 

print(total(5)) 

#user_input = int(input("Enter A Number: "))
#for i in range(user_input - 1, 0, -1):
    #user_input *= i

#print(user_input)