correct_password = "password123"
while True:
    user_input_password = input("Enter The Correct Password: ")
    if user_input_password == correct_password:
        print("Access Grannted")
        break
    else:
        print("Access Denied!")
