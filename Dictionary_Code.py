import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def definition(word):
    word = word.lower()         #change case of word to lower
    if word in data:
        return data[word]        #will return the value of that word(key)
    elif word.title() in  data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:                          #nested loop (nested conditions)
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys()) [0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys()) [0]]
        elif yn == "y":
            return data[get_close_matches(word, data.keys()) [0]]
        elif yn == "N":
            return "This word is not present in the dictionary!"
        elif yn == "n":
            return "This word is not present in the dictionary!"
        else:
            return "We didn't recognise your answer"
    else:
        return "This word is not present in the dictionary!"

word_input = input("Enter word: ")

answer = definition(word_input)

if type(answer) == list:
    for item in answer:
        print(item)
else:
    print(answer)
