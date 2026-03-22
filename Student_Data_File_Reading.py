##OUTPUT.TXT Was Used For A Different Code So This Code Has No Data To Act On!
number_of_students = int(input("Please Input The Number Of Students You'd Like To Input: "))


def func():
    output_file = open("output.txt", 'w')
    for i in range(number_of_students):
        student_name = input("Please Input Student Name: ")
        student_age = input("Please Input Student Age:")
        student_phone_number = input("Please Input Student Phone Number:")
        output_file.write(f"{student_name} {student_age}  {student_phone_number} \n")
    output_file.close()

func()