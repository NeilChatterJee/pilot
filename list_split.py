string = "I am awesome and have really really good grades! and I really like to have pizza for dinner"
print(f"Your Sentence is '{string} '")
count = {}
for item in string.split(" "):
    if item not in count:
        count[item] = 1
    else:
        count[item] += 1
for key, value in count.items():
    print(f"{key} - {value}")