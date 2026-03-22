def get_total_price(list_of_dict):
    for item in list_of_dict:
        tot_price = item["quantity"] * item["price"]
        print(f"Total Price: {tot_price}")



get_total_price([{ "product": "Chocolate", "quantity": 1, "price": 0.10 }, { "product": "Lollipop", "quantity": 3, "price": 0.20 }])
get_total_price([{ "product": "Milk", "quantity": 1, "price": 1.50 }, { "product": "Eggs", "quantity": 12, "price": 0.10 }, { "product": "Bread", "quantity": 2, "price": 1.60 }, { "product": "Cheese", "quantity": 1, "price": 4.50 }])