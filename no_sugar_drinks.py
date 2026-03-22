def healthy_drinks(drink_list):
    sugary_drinks = ["cola", "fanta"]
    healthy_drink = []
    for drink in drink_list:
        if drink.lower() in sugary_drinks:
            continue
        else:
            healthy_drink.append(drink)
    print(healthy_drink)

healthy_drinks(["Cola", "Fanta", "Water", "Juice"])
