count = 0
while True:
    x = int(input("Enter A Number: "))
    count = count + x
    if x == -1:
        break

print(f"Total Input Count Is {count}")