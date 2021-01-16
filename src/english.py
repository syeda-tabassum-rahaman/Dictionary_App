import json 
from difflib import get_close_matches

data = json.load(open("../asset/data/data.json"))

def translate(w):
    w = w.lower() 
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did yoy mean %s insted? If yes enter Y and if no enter N: " % get_close_matches(w,data.keys())[0])
        if yn == "Y":
            return data[ get_close_matches(w,data.keys())[0]]
        elif yn == "N": 
            return " The word doesn't exist. Please check it again."
        else: 
            return " We didn't understand. "
                
    else: 
        return "The word doesn't exist. Please check it again"
word = input("Enter the word: ")
output = translate(word)
 
if type(output) == list:
    for item in output:
        print(item)
else: 
    print(output)