class Code:
    def __init__(self, string, integer):
        self.string = string
        self.integer = integer
    
    def data_type(self):
        if (self.string[0] == "A" 
            or self.string[0] == "B" 
            or self.string[0] == "C" 
            or self.string[0] == "D" 
            or self.string[0] == "E" 
            or self.string[0] == "F" 
            or self.string[0] == "G" 
            or self.string[0] == "H" 
            or self.string[0] == "I" 
            or self.string[0] == "J" 
            or self.string[0] == "K" 
            or self.string[0] == "L" 
            or self.string[0] == "M" 
            or self.string[0] == "N" 
            or self.string[0] == "O" 
            or self.string[0] == "P" 
            or self.string[0] == "Q" 
            or self.string[0] == "R" 
            or self.string[0] == "S" 
            or self.string[0] == "T" 
            or self.string[0] == "U" 
            or self.string[0] == "V" 
            or self.string[0] == "W" 
            or self.string[0] == "X" 
            or self.string[0] == "Y" 
            or self.string[0] == "Z"
        ):
            print("This entered object is a String")
        else:
            print("This entered object is not a String")
    
    def data_type_2(self):
        x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in x:
            if self.integer == x[i]:
                print("This entered object is an Integer")
                return
        print("This entered object is not an Integer")   
    
print(Code("Python", 9).data_type_2())