import random
chances = 10

random_int = random.randint(1, 100)
while True:
    user_guess = int(input("Enter Your Guess! (Must Be A Number, And The Number Must Be 1-100)  : "))
    if user_guess == random_int:
        print("You Got It!")
        break
    elif user_guess > random_int:
        print("Your Guess Is Too High, Guess Again!")
        chances -= 1
        if chances == 0:
            print("You Rand Out Of Chances!")
            break
    elif user_guess < random_int:
        print("Your Guess Is Too Low, Guess Again!")
        chances -= 1
        if chances == 0:
            print("You Ran Out Of Chances!")
            break
            
    print(chances)
        
