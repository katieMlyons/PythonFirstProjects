# load in .json file, take input and return value
import json
from difflib import get_close_matches
search_string=input("Enter word: ")

data=json.load(open("data.json"))

def dict_out(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys())) > 0:
        yn = input("Did you mean %s? Y or N: " % get_close_matches(w,data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w,data.keys(),1)[0]]
        elif yn == "N":
            return "Word not found."
        else:
            return "I don't understand."
    else:
        return "Word not found."

output = dict_out(search_string)
if type(output) == list:
    for i in output:
        print(i)
else: 
    print(output)
