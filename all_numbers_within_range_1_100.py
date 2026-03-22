between_1_and_100 = True
for i in range(0, 10):
    x = int(input("Enter A Number: "))
    if x < 1 or x > 100:
        between_1_and_100 = False

if between_1_and_100 == True:
    print("All Numbers In Range 1-100!")
elif between_1_and_100 == False:
    print("All Numbers Are Not Between 1-100!")