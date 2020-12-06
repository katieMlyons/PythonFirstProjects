# load in .json file, take input and return value
import json
search_string=input("Enter word:")

data=json.load(open("data.json"))

try: print(data[search_string])
except:
    print("Word not found.")
