import json 
from difflib import get_close_matches

data = json.load(open("data.json"))

def Translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif get_close_matches(w, data.keys()):
        yn = input("Did you mean %s here. If yes press Y or if no press N: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please check it again."
        else: 
            return " We don't understand your entry."
    else:
        return "The word doesn't exist. Please check it again."
word = input("Enter the word: ")
output = Translate(word)

if type(output) == list:
    for item in output: 
        print(item)
else:
    print(output)
