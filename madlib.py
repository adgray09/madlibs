words = {}

def store_input ():
    words ["adjective1"] = input("Enter adjective: ")
    words ["noun1"] = input("Enter noun: ")
    words ["adverb1"] = input("Enter adverb ")
    words ["verb1"] = input("Enter verb")
    words ["noun2"] = input("Enter noun")
    words ["noun3"] = input("Enter noun")
store_input()


def print_Madlib():
    print (words["noun1"] + ", all my toubles seem so " + words["adjective1"] + " away ")
    print (words["adverb1"] + " it looks as though they're here to stay")
    print ("oh," + "I " + words["verb1"] + " in yesterday")
    print ("Suddenly, i'm not " + words["noun2"] + " I used to be")
    print ("There's a " + words["noun3"] + " hanging over me")
print_Madlib()