#!/usr/bin/env python
# Works in python2 and python3

"""
Algorithm 17.14 in cracking the coding interview.

Pretty challenging, it took me 1h+ to figure it out and end the code.

Text:
Oh, no! You have just completed a lengthy document when you have
an unfortunate Find/Replace mishap. You have accidentally removed
all spaces, punctuation, and capitalization in the document. A
sentence like "I reset the computer. It still didn't boot!" would
become "iresetthecomputeritstilldidntboot". You figure that you
can add back in the punctuation and capitalization later, once you
get the individual words properly separated. Most of the words will
be in a dictionary but some strings, like proper names, will not.

Given a dictionary (a list of words), design an algorithm to find
the optimal way of "unconcatenating" a sequence of words. In this
case, "optimal" is defined to be the parsing which minimizes the
number of unrecognized sequences of characters. 

For example, the string "jesslookedjustliketimherbrother" would be
optimally parsed as "JESS looked just like TIM her brother". This
parsing has seven unrecognized characters, which we have capitalized
for clarity.

Keys: recursion, dynamic programming.
"""


def calculate_dictionary_permutations(s, d):
    """
    From a sentence s with only lowercase letters (no spaces), and a dictionary
    d with all words known, it returns a list of permutations, where every
    permutation has three fields: the first one is a list of words that make a
    sentence, the second one is the cost of the first N-1 words (where N is the
    number of words in the list of words), and the third one is the cost of the
    last word. The cost refers to the number of characters in words that are not
    found in the dictionary.
    """

    # For only one character, return it as the final word, and calculate cost
    if len(s) == 1:
        return [([s], 0, 0 if s in d else 1)]
    
    # Calculate permutation for all s but last letter
    last = s[-1]
    permutations = calculate_dictionary_permutations(s[:-1], d)

    # Add last letter to all permutations and calculate new costs
    # Note that we only record new sentences if their costs are lower than the old ones
    costs = {}
    my_permutations = []
    for p in permutations:
        prefix, cost_first, cost_last = p
        
        # Add last letter as separate word after the sentence
        new_cost_first = cost_first + cost_last
        if last not in costs or new_cost_first < costs[last]:
            new_prefix1 = prefix + [last]
            my_permutations.append([new_prefix1, new_cost_first, 0 if last in d else 1])
            costs[last] = new_cost_first
        
        # Add last letter as letter at the end of last word in sentence
        new_last = prefix[-1] + last
        if new_last not in costs or cost_first < costs[new_last]:
            new_prefix2 = prefix[:]
            new_prefix2[-1] = new_last
            my_permutations.append([new_prefix2, cost_first, 0 if new_last in d else len(new_last)])
            costs[new_last] = cost_first
    
    # Delete permutations with cost higher than the one recorded in costs
    i = 0
    while i < len(my_permutations):
        prefix, cost_first, cost_last = my_permutations[i]
        if cost_first > costs[prefix[-1]]:
            del my_permutations[i]
        else:
            i += 1
    
    # Return permutations obtained
    return my_permutations
    

def split_string_by_dictionary(s, d):
    """
    s is a string with only lowercase letters, d is a dictionary of words (a set)
    
    We return s with spaces added, making sure that we minimize the number of characters
    outside of words not in the dictionary. For example, assuming we have in a dictionary
    most words in the English language, we would get from:
    jessandbenarefrineds --> JESS and BEN are friends (cost = 7).
    The words capitalized are the ones not found in the dictionary.
    """
    permutations = calculate_dictionary_permutations(s, d)
    best_cost = len(s) + 1
    best_sentence = None
    for p in permutations:
        cost = p[1] + p[2]
        words = p[0]
        if best_cost > cost:
            best_cost = cost
            best_sentence = words
    final_sentence = ""
    prev_upper = False
    for word in best_sentence:
        if word not in d:
            final_sentence += ("" if prev_upper else " ") + word.upper()
            prev_upper = True
        else:
            final_sentence += " " + word
            prev_upper = False
    return final_sentence[1:], best_cost


if __name__ == "__main__":
    s = "hellomynameisdanielandiamwithdevanshu"
    d = {"hello", "my", "name", "is", "and", "i", "am", "with", "paper", "computer", "pikachu"}
    print("INPUT:")
    print("Dictionary: {}\nString: {}".format(d, s))
    print("\nOUTPUT:")
    sentence, cost = split_string_by_dictionary(s, d)
    print("Sentence: {}\nCost: {}", sentence, cost)