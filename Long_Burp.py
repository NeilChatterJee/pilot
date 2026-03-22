how_long = int(input("Input How Many Rs You Want: "))
def long_burp():
    burp = "Burp"
    number_of_rs = "r" * how_long
    burp_modified = burp[0:2] + number_of_rs + burp[-1]
    print(burp_modified)

long_burp()