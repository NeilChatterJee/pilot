#Q1
names_list = ["Ada", "William", "Ursula", "Ellie", "Unova", "Otto", "Zack", "Tom", "Aum", "Nihkil", "Hamza", "Pratyush", "Sasmit"]
vowels_list = []
consonant_list = []

for i in names_list:
    if (i[0].lower() in ['a', 'e', 'i', 'o', 'u']):
        vowels_list.append(i)
    else:
        consonant_list.append(i)
        
print(vowels_list)
print(consonant_list)

#Q2
list_string = ["abacada", "13456", "mmiabn", "8945"]
digit_only = []
mixed_characters = []

for i in list_string:
    if i.isdigit():
        digit_only.append(i)
    else:
        mixed_characters.append(i)
print(digit_only)
print(mixed_characters)


#Q3
file_names = ["monkey.txt", "dude", "work.txt", "python.txt", "plans", "vacation.txt"]
files_with_txt = []
for i in file_names:
    if i.endswith(".txt"):
        files_with_txt.append(i)
    
print(files_with_txt)
files_with_txt.clear()
i = 0
while (i < len(file_names)):
    element = file_names[i]
    if element.endswith(".txt"):
        files_with_txt.append(element)
    i =  i + 1
print(files_with_txt)


#Q4

y = ["ada", "William", "Nihkil", "Neil", "Ursula", "malayalam"]
x = []
def break_down(y):
    for i in y:
        if i.lower() == (i[::-1]).lower():
            x.append(i)
    print(x)

break_down(y)


def palindrome(y):
    i = 0
    x = []
    while (i < len(y)):
        element = y[i]
        if element.lower() == (element[::-1].lower()):
            x.append(element)
        i = i + 1
    print(x)
palindrome(x)

#Q5(1st)
data = [1, 3, 6, 7, 9, 15, 21, 17, 36]
number_of_numbers_divisible_by_3 = 0
for i in data:
    if i % 3 == 0:
        number_of_numbers_divisible_by_3 += 1
print("Q5(1st): ", number_of_numbers_divisible_by_3)

i = 0
counter = 0
while (i < len(data)):
    element = data[i]
    if element % 3 == 0:
        counter = counter + 1
    i = i + 1
print(f"The count of numbers divisible by 3 is {counter}")

#Q5(2nd)
number_list = [0,1,2,6,8,3,5,9,11,15]
for i in range(len(number_list)):
    if number_list[i] % 2 != 0:
        number_list[i] = 0

print("Q5(2nd): ", number_list)

i = 0
number_list = [0,1,2,6,8,3,5,9,11,15]
while (i < len(number_list)):
    if number_list[i] % 2 != 0:
        number_list[i] = 0
    i = i + 1
print(number_list)




#Q6
numbers = [30, 10, 15, 20, 10, 20, 50, 30]
total_sum = 0
for num in numbers:
    total_sum += num
    print("Q6: ", total_sum, num)
    if total_sum > 100:
        break
print(f"The sum is over 100 now, the total is {total_sum}")

i = 0 
entire_total = 0
while (i < len(numbers)):
    element = numbers[i]
    entire_total += element
    if entire_total > 100:
        break
    i = i + 1
print(f"The entire total is {entire_total}")

#Q7
even_or_odd =  [12, 7, 9, 14, 22, 31, 40, 55, 60]
even_numbers = 0
odd_numbers = 0
for i in even_or_odd:
    if i % 2 == 0:
        even_numbers += 1
    else:
        odd_numbers += 1

print(f"The count of even numbers is {even_numbers}")
print(f"The count of odd numbers is {odd_numbers}")

x  = 5
while (True):
    print(x)
    x = x + 5
    if x  >50:
        break


y = 7
while (True):
    print(y)
    y = y + 7
    if y > 98:
        break



while (True):
    number = int(input('Enter a number, press -100 for exit:'))
    if (number == -100):
        break
    else:
        if (number %2 == 0):
            print(f"{number} is even")
        else:
            print(f"{number} is odd")

#Topic To Study For Next Class
"how to convert list into string"
"how to convert string into list"