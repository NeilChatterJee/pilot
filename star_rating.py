def get_item(dict, star_rating):
    for key in dict:
        if dict[key] == star_rating:
            print(f"{key}: {star_rating}")
        

dictionary = { 
    "Luxury Chocolates" : "*****", 
    "Tasty Chocolates" : "****",
    "Aunty May Chocolates" : "*****", 
    "Generic Chocolates" : "***" 

}


get_item(dictionary, "*****")