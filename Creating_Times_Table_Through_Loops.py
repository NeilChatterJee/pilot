number_for_table = int(input("Please Input Which Number You Want For A Times Table: "))
table_number_to_stop_at = int(input("Input Which Number You Want The Table To Stop At: "))


def times_table():
    i = 1
    
    output_file = open("output.txt", 'w')
    while i <= table_number_to_stop_at:
        table = number_for_table * i
        output_file.write(f"{table} \n")
        i = i + 1
    output_file.close()



times_table()