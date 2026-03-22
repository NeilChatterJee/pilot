#Q1
input_string = input("Enter a string: ")
if (input_string.strip()) == "":
    print("The string is empty.")
else:
    print("The string is not empty.")

#Q2
input_string = input("Enter a string: ")
# solution 1
vowelList = ['a', 'e', 'o', 'i', 'u']
if (input_string[0].lower() in vowelList):
    print("The string starts with a vowel.")
else:
    print("The string does not start with a vowel.")

# solution 2
if (input_string[0].lower()) == "a" or (input_string[0].lower()) == "e" or (input_string[0].lower()) == "o" or (input_string[0].lower()) == "i" or (input_string[0].lower()) == "u":
    print("The string starts with a vowel.")
else:
    print("The string does not start with a vowel.")

#Q3
input_string = input("Enter a string: ")
if input_string.endswith(".com"):
    print("Commercial Site")
elif input_string.endswith(".org"):
    print("Organization Site")
else:
    print("Unknown Site")

#Q4
input_string = input("Enter a string: ")
if (input_string[0].lower()) == (input_string[-1].lower()):
    print("The first and last characters are the same.")
else:
    print("The first and last characters are not the same.")

#Q5
y = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(len(y) // 2)
input_string = input("Enter a string: ")
length = len(input_string)
if length % 2 != 0:  
    middle_index = length // 2
    print(f"The middle character is: {input_string[middle_index]}")
else:  
    print("The Length is Even")

#Q6
input_string = input("Enter a string: ")
word_to_check = input("Enter the word to check: ")
if word_to_check in input_string:
    print(f"The string contains the word {word_to_check}.")
else:
    print(f"The string does not contain the word {word_to_check}.")

#Q7
input_string = input("Enter a string: ")
if input_string == input_string[::-1]:
    print("string is a palindrome")
else:
    print("string is not a palindrome")

#Q8
input_string = input("Enter a string: ")
if len(input_string) < 5:
    print("Too short")
else:
    print(f"The last 3 characters are: {input_string[-3:]}")

#Q9
input_string = input("Enter a string: ")
if input_string.isupper():
    print("Uppercase")
elif input_string.islower():
    print("Lowercase")
else:
    print("Mixed")

#Q10
input_string = input("Enter a string: ")
if input_string.isdigit():
    print("The string contains only digits.")
else:
    print("The string does not contain only digits.")

#LIST SECTION

#Q1
homework_list = input()
length = len(homework_list)
if length == 0:
    print("List is empty")
else:
    print("List is not empty")

#Q2
homework_list2 = input()
length = len(homework_list2)
if length == 0:
    print("No Elements")
else: 
    print(homework_list2[0])

#Q3
list_input= [5,10,11,45,68]
if 5 in (list_input):
    print("Specific Value Not in List")
else:
    print("Specific Value In List")

#Q4
x = [1,2,3,4,5,6,7,8,9,10]
y = [3, 5, 6, 8, 9, 67, 58, 589, 5860, 59, 56, 78]
length = len(x)
length2 = len(y)
if length > length2:
    print("x is greater y")
elif length == length2:
    print("Length of X is equal to Length of Y")
else:
    print("Length of Y is greater than Length of X")

#Q5
my_list = [1, 2, 3, 4]
if len(my_list) >= 3:
    print("The list has at least 3 elements.")
else:
    print("The list does not have at least 3 elements.")

#Q6
my_list = [1, 2, 3]
if len(my_list) >= 2:
    result = my_list[0] + my_list[1]
    print("Sum of the first two elements:", result)
else:
    print("Not enough elements")

#Q7
my_list = [1, 2, 3, 2, 1]
if my_list == my_list[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")

#Q8
my_list = [1, 2, 3]
if len(my_list) > 0:
    print(my_list[-1])  # Return the last element
else:
    print("Empty List")

#Q9
my_list = [1, -2, 3, 4]
for i in my_list:
    if i > 0:
        print("All elements are positive numbers.")
    else:
        print("Not all elements are positive numbers.")

#Q10
if len(my_list) == 3:
    product = my_list[0] * my_list[1] * my_list[2]
    print(product)
else:
    print("Not 3 elements")