def get_median(list):
    list.sort()
    len_list = len(list)
    if len_list % 2 == 0:
        x = len_list // 2
        y = x + 1
        z = (int(list[x]) + int(list[y])) / 2
        print(z)
    else:
        med_pos = len_list // 2
        med_pos_1 = int(med_pos)
        median = list[med_pos_1 + 2]
        print(median) 

def get_mode(list):
    mode = list[0]
    most_common = 0
    for values in list:
        count_sum = list.count(values)
        if count_sum > most_common:
            most_common = count_sum
            mode = values
    print(f"Mode: {mode}")

    
    
            
user_list = input("Enter Any Amount Of Numbers(Comma Separated): ")
input_list = user_list.split(",")


get_mode(input_list)