list_1 = ["a", "c", "d", "g", "l"]
input = input("What would you like to find: ")
j = 0
for i in list_1:
    if i == input:
        print(f" This item's position in the array is {j}")
        break
    else:
        j += 1