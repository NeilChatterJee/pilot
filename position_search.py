ghf = [2,4,5,8,9,3,6,10]
user_input = int(input("Enter The Number You'd Like To Search For: "))
tr = True
for values in ghf:
    if user_input == values:
        x = ghf.index(user_input)
        print(f"Your Number's Position is {x}")
        tr = False
        break
if tr == True:
    print("Number Not In List")