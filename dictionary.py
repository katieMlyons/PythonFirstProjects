# load in .json file, take input and return value
import json
from difflib import get_close_matches
search_string=input("Enter word:")

data=json.load(open("data.json"))

def dict_out(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys(),1))>0:
        answer = input("Did you mean {}? Y or N:".format(get_close_matches(w,data.keys(),1)[0]))
        if answer.lower() == "y":
            return data[get_close_matches(w,data.keys(),1)[0]]
        elif answer.lower() == "n":
            return "Word not found."
        else:
            return "I don't understand."
    else:
        return "Word not found."

if type(dict_out(search_string)) == list:
    for i in dict_out(search_string):
        print(i)
else: 
    print(dict_out(search_string))
