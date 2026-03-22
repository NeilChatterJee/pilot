def string_reverse_casing(string):
    new_string = ""
    for char in string:
        if char.isupper():
            new_string = new_string + char.lower()
        elif char.islower():
            new_string = new_string + char.upper()
    print(new_string)

string_reverse_casing("Neil Chatterjee")
string_reverse_casing("sPoNtAnEoUs")
string_reverse_casing("MANY THANKS")
string_reverse_casing("Happy Birthday")