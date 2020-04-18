import json
import difflib
from difflib import get_close_matches
data = json.load(open("yourjsonfile.json"))
#print(data)

def find_closest(word):
    mylist=get_close_matches(word,data.keys(),0.85)
    print(mylist)
    if len(mylist) == 0:
        return "no close word found"
    else :
        return mylist[0]

def find_meaning(word):
    if word in data:
        return data[word]
    
    word=word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        close_word=find_closest(word)
        if close_word == "no close word found":
            return "word not in dictionary"
        else:
            user_prompt = 'did you mean "%s" instead ?type Y to continue: ' % close_word
            choice=input(user_prompt)
            if choice=="Y":
                return data[close_word]
            else:
                return "word not in dictionary"
        
        

word=input("enter word : ")
meaning=find_meaning(word)
if(type(meaning)==list):
    for meanings in meaning:
        print(meanings)
else: 
    print(meaning)





