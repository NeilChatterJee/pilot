def get_budgets(list_of_dicts):
    x = 0
    for item in list_of_dicts:
        x += item["budget"]
    print(f"Total Budget: {x}")
get_budgets([{ "name": "John","age": 21, "budget": 29000 }, { "name": "Steve","age": 32, "budget": 32000 }, { "name": "Martin","age": 16, "budget": 1600 }])