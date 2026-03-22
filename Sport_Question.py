sports_info = {
    "cricket": [["What does IPL stand for?", ],
                [], 
                []],
    "Study": {[[], []]} 
         }
    


    

questions = sports_info["cricket"]["Question 1"]
options = sports_info["cricket"]["options_1"]

print(f"Question: {questions}")
print(f"options: {options}")
user_choice = input("Please choose from the answers above (type them in the exact same way): ")

final_score = 0

if user_choice.lower() == sports_info["cricket"]["answer_1"].lower():
    final_score += 1
    

questions_2 = sports_info["cricket"]["Question 2"]
options_2 = sports_info["cricket"]["options_2"]

print(f"Question: {questions_2}")
print(f"options: {options_2}")
user_choice2 = input("Please choose from the answers above (type them in the exact same way): ")

if user_choice2.lower() == sports_info["cricket"]["answer_2"].lower():
    final_score += 1

print(f"Final Score: {final_score}")


