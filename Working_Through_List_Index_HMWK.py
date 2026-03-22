#HMWK Question 4
z = ["Delhi", "Mumbai", "Chennai", "Kolkata", "Patna", "Ranchi"]
index = z.index("Patna")
print(f"Patna's index is {index}")
z.pop(index+1)
print(z)

#HMWK Question 5
I = ["Delhi", "Mumbai", "Chennai", "Kolkata", "Patna", "Ranchi"]
I.append("Jaipur")
print(I)

#HMWK Question 6
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(x[ : -6])
print(x[4 : ])
print(x[4: -4])