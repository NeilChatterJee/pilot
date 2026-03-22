x = [["Neil", "Dave", "Krishna", "Siddhart", "Aum", "Pratyush", "Nagadhar", "Muralidhar", "Johnathan", "Clark"], 
     [91, 92, 86, 97, 98, 100, 32, 33, 56, 65], 
     [25, 30, 36, 38, 42, 43, 50, 48, 47, 49], 
     [50]]
print (f"Name : {x[0][1]}, Marks : {x[1][1]}, Attendance is {x[2][1]} out of {x[3][0]}")

# Name : Neil, Marks : 91, Attendance 25 out of 50
# using class object

y = {
    "USA" : "Washington",
    "Australia" : "Canberra",
    "Austria" : "Vienna",
    "China" : "Beijing",
    "Japan" : "Tokyo",
    "Russia" : "Moscow",
    "Germany" : "Berlin",
    "Philipines" : "Manila",
    "Indonesia" : "Jakarta",
    "Nigeria" : "Lagos",
    "Thailand" : "Bangkok",
    "India" : "New Delhi",
    "Tanzania" : "Dodoma",
    "Bangladesh" : "Chittagong",
    "Mexico" : "Mexico City"
}

print(y.keys())
print(y.values())
y["Italy"] = "Rome"
y.pop("India")
print(y)

y["Italy"] = "Mumbai"
print(y.values())

y.clear
print(y)


