#song lyrics from the Beatles called Yesterday

words = {}

def store_input ():
    words ["noun1"] = input("Enter noun: ")
    words ["adjective1"] = input("Enter adjective: ")
    words ["adverb1"] = input("Enter adverb ")
    words ["verb1"] = input("Enter verb")
    words ["noun2"] = input("Enter noun")
    words ["noun3"] = input("Enter noun")
    words ["adverb2"] = input("Enter adverb")
    words ["pronoun1"] = input("Enter pronoun")
    words ["adjective2"] = input("Enter adjective")
store_input()


def print_Madlib():
    print (words["noun1"] + ", all my toubles seem so " + words["adjective1"] + " away ")
    print (words["adverb1"] + " it looks as though they're here to stay")
    print ("oh," + "I " + words["verb1"] + " in yesterday")
    print ("Suddenly, i'm not " + words["noun2"] + " I used to be")
    print ("There's a " + words["noun3"] + " hanging over me")
    print ("Oh, yesterday came " + words["adverb2"])
    print ("Why " + words["pronoun1"] + " had to go I don't know she wouldn't say")
    print ("I said something " + words["adjective2"] + ", now I long for yesterday")
print_Madlib()