def get_2_unique_num(repeating_list):
    dict = {}
    for item in repeating_list:
        if item in dict:
            dict[item] += 1
        else:
            dict[item] = 1
    for key, value in dict.items():
        if value == 1:
            print(key)

list_1 = [1, 9, 8, 8, 4, 5, 5]
get_2_unique_num(list_1)