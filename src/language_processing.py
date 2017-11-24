import sys



def find_match(my_dict,utterance):
    for key in my_dict:
        if key in utterance:
            return my_dict[key]
    return None
