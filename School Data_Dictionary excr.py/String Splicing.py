#Dictionary Question
school_dict1 = {
    "Class1": {
        "Neil": {
            "Math": 98,
            "English": 92,
            "Social Studies": 93,
            "Science": 98,
            "Robotics": 100
        },
        "Sasmit": {
            "Math": 92,
            "English": 97,
            "Social Studies": 98,
            "Science": 95,
            "Economics": 93
        },
        "Aum": {
            "Math": 91,
            "English": 89,
            "Social Studies": 78,
            "Science": 64,
            "Robotics": 100
        },
        "Mukund": {
            "Math": 86,
            "English": 94,
            "Social Studies": 96,
            "Science": 76,
            "Robotics": 103
        },
        "Tejas": {
            "Math": 45,
            "English": 96,
            "Social Studies": 54,
            "Science": 73,
            "Robotics": 91
        }
    },
    "Class2": {
        "Alice": {
            "Math": 88,
            "English": 76,
            "History": 93,
            "Biology": 87,
            "Chemistry": 94
        },
        "Bob": {
            "Math": 82,
            "English": 84,
            "History": 91,
            "Biology": 79,
            "Chemistry": 88
        },
        "Charlie": {
            "Math": 90,
            "English": 85,
            "History": 92,
            "Biology": 80,
            "Chemistry": 96
        },
        "David": {
            "Math": 91,
            "English": 79,
            "History": 94,
            "Biology": 81,
            "Chemistry": 87
        },
        "Eva": {
            "Math": 85,
            "English": 80,
            "History": 88,
            "Biology": 83,
            "Chemistry": 92
        }
    },
    "Class3": {
        "John": {
            "Math": 95,
            "English": 90,
            "Geography": 88,
            "Physics": 92,
            "Chemistry": 97
        },
        "Sophie": {
            "Math": 93,
            "English": 86,
            "Geography": 85,
            "Physics": 91,
            "Chemistry": 94
        },
        "Lucas": {
            "Math": 88,
            "English": 80,
            "Geography": 92,
            "Physics": 85,
            "Chemistry": 96
        },
        "Maya": {
            "Math": 87,
            "English": 94,
            "Geography": 89,
            "Physics": 93,
            "Chemistry": 99
        },
        "Oliver": {
            "Math": 91,
            "English": 88,
            "Geography": 90,
            "Physics": 84,
            "Chemistry": 95
        }
    },
    "Class4": {
        "Ella": {
            "Math": 79,
            "English": 85,
            "Art": 92,
            "Computer Science": 97,
            "Music": 88
        },
        "Liam": {
            "Math": 82,
            "English": 90,
            "Art": 88,
            "Computer Science": 85,
            "Music": 92
        },
        "Emma": {
            "Math": 94,
            "English": 89,
            "Art": 90,
            "Computer Science": 92,
            "Music": 97
        },
        "Ava": {
            "Math": 88,
            "English": 84,
            "Art": 91,
            "Computer Science": 93,
            "Music": 85
        },
        "Mason": {
            "Math": 85,
            "English": 86,
            "Art": 87,
            "Computer Science": 94,
            "Music": 91
        }
    },
    "Class5": {
        "Ethan": {
            "Math": 91,
            "English": 89,
            "Economics": 92,
            "Art": 95,
            "Computer Science": 98
        },
        "Isabella": {
            "Math": 88,
            "English": 93,
            "Economics": 90,
            "Art": 87,
            "Computer Science": 94
        },
        "James": {
            "Math": 94,
            "English": 85,
            "Economics": 91,
            "Art": 92,
            "Computer Science": 97
        },
        "Mia": {
            "Math": 86,
            "English": 84,
            "Economics": 88,
            "Art": 93,
            "Computer Science": 90
        },
        "Benjamin": {
            "Math": 90,
            "English": 91,
            "Economics": 87,
            "Art": 95,
            "Computer Science": 92
        }
    }
}



print(school_dict1["Class1"]["Neil"]["Math"])



#Q1
x = "I Hate Vegetables"
y = x.split()
print(y)

#Q2-3
z = "India is good"
print(z.replace("India", "America"))
print(z.upper())
print(z.lower())

#Q4
f = "India is best Country"
q = "India, Is, Best, Country"
n = "India ; Is ; Best ; Country;"
g = f.split()
print(g)
r = q.split(",")
print(r)
m = n.split(";")
print(m)
print(g[0])
print(g[-1])

#Q5
h = "I Eat Pizza"
k = len(h.split())
print(k)

#Q6
v = "    Coding is Good        "
print(v.strip())