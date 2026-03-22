def mapping(user_list):
    dict = {}
    for item in user_list:
        dict[item] = item.upper()

    print(dict)



mapping(["a", "b", "c", "d", "e"])