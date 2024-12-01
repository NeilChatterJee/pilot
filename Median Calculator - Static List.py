print " Five Inputs Maximum, And They Have To Be In Order"
x = []
for i in range(0,5):
  x.append(input())

print(x)
print("Len", len(x))
def median(y):
  if len(x) % 2 == 0:
    mid1 = (len(x) / 2) - 1 
    print("mid1", mid1)
    print(x[mid1])
    mid2 = len(x) / 2 
    print("mid2", mid2)
    med = (x[mid1] + x[mid2]) / 2.0
    print(med)
    return (mid1, mid2)
  else:
    mid = len(x) / 2
    print("mid", x[mid])
    return (mid)
       
    print(median)