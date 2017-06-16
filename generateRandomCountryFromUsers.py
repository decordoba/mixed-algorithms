#!/usr/bin/env python2

"""
From a Google Interview
The question was not well designed, and I solved it in 2 min with country_random_generator1
which has constant time complexity and is the fastest solution.

My interviewer wanted me to do some kind of binary search, like it is done in country_random_generator2
but the only reason to do it in this way is if the input was some kind of hash table with the number
of appearances of every country instead of a country list. Anyway, both solutions are shown below.
"""

import random
from basic import *  # Find basic.py in https://github.com/decordoba/basic-python


def country_random_generator1(countries=None, random_pos=None, verbose=False):
    if countries is None:
        countries = ["Spain", "Usa", "China", "Usa", "Usa"]
    num_users = len(countries)
    if random_pos is None:
        random_pos = int(random.random() * num_users)
    else:
        random_pos = random_pos % num_users
    return countries[random_pos]

def country_random_generator2(countries=None, random_pos=None, verbose=False):
    if countries is None:
        countries = ["Spain", "Usa", "China", "Usa", "Usa"]
    
    country_names_ht = {}
    country_names = []
    country_number = []
    for c in countries:
        if c in country_names_ht:
            country_number[country_names_ht[c]] += 1
        else:
            country_names_ht[c] = len(country_names)
            country_names.append(c)
            country_number.append(1)
    
    cum_country_number = []
    prev = 0
    for c in country_number:
        prev += c
        cum_country_number.append(prev)
    
    num_users = cum_country_number[-1]  # Or len(countries)
    if random_pos is None:
        random_pos = int(random.random() * num_users)
    else:
        random_pos = random_pos % num_users
    
    idx0 = 0
    idx1 = len(country_names) - 1
    while idx0 < idx1:
        new_idx = (idx1 + idx0) // 2
        current_pos = cum_country_number[new_idx]
        if current_pos > random_pos:
            idx1 = new_idx
        elif idx0 == new_idx:
            idx0 += 1
        else:
            idx0 = new_idx
    result = country_names[idx0]

    if verbose:
        print ("Countries: " + " {:^10}" * len(country_names)).format(*country_names)
        print ("Users:     " + " {:^10}" * len(country_number)).format(*country_number)
        print ("Cumulative:" + " {:^10}" * len(cum_country_number)).format(*cum_country_number)
        print "Random Pos: {}".format(random_pos)
        print "Result:     {}".format(result)

    return result

    
if __name__ == "__main__":
    default = "Spain Usa France Usa Spain India China China India India China Usa Usa Usa Canada China China China China China India"
    input = readInputArguments(input=default)
    parsed_input = parseString(input)[0]
    r1 = country_random_generator1(parsed_input, verbose=True)
    r2 = country_random_generator2(parsed_input, verbose=True)
