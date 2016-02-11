#!/usr/bin/python
# -*- coding: latin-1 -*-
"""
markov chain experimentation

call by giving a original set of word to start with (more than nbrkey)

The program cut the given text by word, based on space
It takes a certain number (nbrkey) of following words, for instance two
by two, and associate to this tuple another sequence of word of length
nbrvalue
finally it create a dictionary based on these associations and chain
them to generate the text

I personally populate "text_data.txt" with http://norvig.com/big.txt

Also try to use https://gist.github.com/yanofsky/5436496
"""

import sys
import random


FILENAME = "nemecle_tweets.csv"


def dict_search(dictionnary, word):
    """
    search for multiple tuples and return them as a list

    """

    returnlist = []

    try:
        for (key, value) in dictionnary:
            if word.endswith(key):
                returnlist.append((key, value))

    except Exception as exp:
        print "(search) Error while working with dictionary: " + str(exp)

    return returnlist

def main():
    """
    main function of the program

    """

    # variable initialization
    length = 100

    if len(sys.argv) < 3:
        print("please call the script with two numbers as argument.")
        sys.exit(2)

    try:
        nbrkey = int(sys.argv[1])
        nbrvalue = int(sys.argv[2])
    except Exception:
        print("please call the script with two numbers as argument.")
        sys.exit(2)

    try:
        #3rd argument is optional
        length = int(sys.argv[3])
    except Exception:
        pass


    try:
        with open(FILENAME, 'r') as data:
            text = data.read()
    except Exception as exp:
        print("(main) Error while reading file: " + str(exp))

    endstring = ""
    wordtuples = []
    isoutofdata = False
    ite = 0

    print("striping unwanted characters")
    for char in ["\"", ")", "(", "]", "[", "="]:
        text = text.replace(char, '')
    text = text.split()
    numberofword = len(text)


    # feeding data
    print("creating tuples")
    for nbr in range(0, numberofword - nbrkey - nbrvalue):
        keywords = []
        valuewords = []
        for key in range(nbr, nbr + nbrkey):
            keywords.append(text[key])
        for key in range(nbr + nbrkey, nbr + nbrkey + nbrvalue):
            valuewords.append(text[key])


        keywords = ''.join(str(e) + " " for e in keywords)
        keywords = " ".join(keywords.split())

        valuewords = ''.join(str(e) + " " for e in valuewords)
        valuewords = " ".join(valuewords.split())

        # print "\"" + keywords + "\" \"" + valuewords + "\""

        wordtuples.append((keywords, valuewords))

        # print(str(nbr) + " tuples created")


    print("starting with seed")
    seed, _ = random.choice(wordtuples)
    endstring += seed

    print("starting adding samples")
    while not isoutofdata and ite < length:
        lastword = " ".join(endstring.split()[-nbrkey:])
        possibilities = dict_search(wordtuples, lastword)
        if len(possibilities) is 0:
            isoutofdata = False
        else:
            (key, value) = random.choice(possibilities)

            endstring += " " + value

            ite += 1
            # print("is at " + str(ite) + " iteration")

    print("finished after " + str(ite) + " iteration")
    print("result is: ")
    print(endstring)

    sys.exit(0)

if __name__ == '__main__':
    main()
