def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit



#Now write your function for converting Fahrenheit to Celsius.
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

conversion_type = input("Which Conversion Type Would You Like? (Type Fahrenheit For Celcius to Fahrenheit, And Vice Versa For Celcius) : ")
conversion_degrees = float(input("What Temperature Number Would You Like To Convert? : "))

if conversion_type.lower() == "celcius":
    fahrenheit_to_celsius(conversion_degrees)
    print(f"{conversion_degrees} fahrenheit is {fahrenheit_to_celsius(conversion_degrees)} celcius!")
elif conversion_type.lower() == "fahrenheit":
    fahrenheit_to_celsius(conversion_degrees)
    print(f"{conversion_degrees} degrees celcius is {celsius_to_fahrenheit(conversion_degrees)} degrees fahrenheight!")