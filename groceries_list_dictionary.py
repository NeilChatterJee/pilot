grocery_dict_1 = {
    "Carrot": "$19.82",
    "Apple" : "$14.53",
    "Banana" : "$4.56"

}


user_input = ("Enter Any Input")
if user_input in grocery_dict_1:
    print(True)
else: 
    print(False)

dict = {
    "upvotes": 98,
    "downvotes" : 45
}

def voting(voting_dict):
    vote_count = voting_dict["upvotes"] - voting_dict["downvotes"]
    print(vote_count)

voting(dict)
