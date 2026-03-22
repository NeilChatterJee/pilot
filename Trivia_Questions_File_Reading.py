def question_data():
    Data_base = {
    
    }
    print(Data_base)

question_data()


file = open('input.txt','r')
lines = file.readlines()
for line in lines:
    line = line.strip().split(",")
if (len(line) == 7):
    genre = line[0]
    question = line[1]
    options = line[2:6] 
    answers = line[6]


