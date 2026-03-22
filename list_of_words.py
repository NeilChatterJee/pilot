def count_words_list(list_of_words, sample_string):
    count_dict = {

    }
    string_list = sample_string.split(" ")
    for word in list_of_words:
        count = 0
        for t in string_list:
            if word == t.lower():
                count += 1
        count_dict[word] = count
    print(count_dict)
words_list = ["python", "code", "practice"] 
text = "Python is great for coding. Students practice Python code every day to improve their coding skills." 
 
count_words_list(words_list, text)  