string = "Neil is learning Python"
count_values = {}
for item in string:
    if item not in count_values:
        count_values[item] = 1
    else:
        count_values[item] += 1
for item in count_values:
    print(f"{item} - {count_values[item]}")