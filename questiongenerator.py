from wordLoader import wordLoader
import random
from random import choice

def giveRandomEntry(wordlist):
    value = choice(list(wordlist.values()))
    print("\n" + value)
    return value

def askAnswer():
    answer = input("Give answer: ")
    return answer

def getSolution(wordlist, val):
    for key, value in wordlist.items(): 
         if val == value: 
             return key 
    return "key doesn't exist"



def main():
    wordlist = wordLoader().getWordlist()
    while(True):
        value = giveRandomEntry(wordlist)
        answer = askAnswer().lower()
        correct = getSolution(wordlist,value).lower()

        if (answer == correct):
            print("\n CORRECT")
        else:
            print("\n Wrong answer, solution is: \n " + correct)





if __name__ == "__main__":
    main()