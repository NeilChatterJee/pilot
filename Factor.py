def factor():
    number_of_factors = 0
    total = 0
    x = int(input("Please Input An Integer: "))
    for i in range(1,100):
        if x % i == 0:
            number_of_factors += 1
            total = total + i
            print(i)
    print(f"The Numbers Above Are Factors Of {x}: ")
    if number_of_factors == 2 and total == 1 + x:
        print(f"{x} is prime!")
    else:
        print(f"{x} is not a prime number!")
    print(f"The number of factors {x} has is {number_of_factors}")
    print(f"The Sum Of Your Factors Is {total}")
        


factor()

