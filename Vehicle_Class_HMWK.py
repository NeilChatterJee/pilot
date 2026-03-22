class Vehicle:
    def __init__(self, type, brand, model, price):
        self.type = type
        self.brand = brand
        self.model = model
        self.price = price
        

    def mode(self):
        if self.type[0] == "A" or self.type[0] == "a":
            print("Air_Vehicle")
        elif self.type[0] == "W" or self.type[0] == "w":
            print("Water Vehicle")
        else:
            print("Ground Vehicle")
    
print(Vehicle("Warship", "Ford", "X", 15000).mode())