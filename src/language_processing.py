import sys


## find_match: takes each key in dictionary and matches it in the string set.  O(n*m)
## It will stop when a key is found.
## if keys collide or compete there will be a problem.


def find_match(my_dict,utterance):
    for key in my_dict:
        if key in utterance:
            return my_dict[key]
    return None




###   Filler Phrases
##    Keyword phrases
##    Parameter phrases
##    More of a grammar
##    Construct a tree

##  { "action":None, "object":{"type":None  "details":None}}
##  Example:
##  

