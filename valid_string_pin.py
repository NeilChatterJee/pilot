def string__pin_validater():
    re_entered_correctly = 0
    alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    empty_space = " "
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    print("         RULES       ")
    print("1. Pin Must Only Contain Numbers!")
    print("2. Pin Must Only Be 4 or 6 Characters Long!")
    print("3. Pin Must Not Have ANY Empty Space!")

    user_pin = input("Enter any Pin: ")

    # Check length 
    while len(user_pin) != 4 and len(user_pin) != 6:
        user_pin = input("Your Pin's Length Is Invalid. Re-Enter Your Pin: ")
    print("The Pin Has A Valid Length.")

    # Check for letters
    has_letter = False
    for char in user_pin:
        if char.lower() in alphabet_list:
            has_letter = True
            break
    while has_letter:
        user_pin = input("The Pin Is Not Allowed To Have Letters! Re-Enter Your Pin: ")
        has_letter = False
        for char in user_pin:
            if char.lower() in alphabet_list:
                has_letter = True
                break
    print("This Pin Is Valid As It Does Not Contain Letters!")

    # Check for empty spaces
    while empty_space in user_pin:
        user_pin = input("This Pin Contains An Empty Space! Re-Enter Your Pin: ")
    print("This Pin Is Valid As It Does Not Contain Empty Spaces!")

    # Check if only numbers
    valid_pin = True
    for ch in user_pin:
        if ch not in digits:
            valid_pin = False
            break
    if valid_pin:
        print("Yay! The Pin Is Fully Valid!")
    else:
        print("Womp Womp! The Pin Contains Invalid Characters!")


# Run the function
string__pin_validater()