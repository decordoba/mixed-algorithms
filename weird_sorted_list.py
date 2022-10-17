"""
Problem (from an interview of a friend):
We have a sorted list of numbers: ["8", "6", "2", "94", "39", "57", "56", "60", "467", "072", "333", "299"]
The problem is that the relationships between numbers are unknown, for example, 7 might be smaller than 1 but greater than 2.
We then are given 2 numbers besides the list, and we need to say which one is bigger, or if we can't tell, based on the list.
Also, I would like to catch if there are inconsistencies in the sorted list, although that was not part of the problem.
"""


def get_rules_sorted_list(s):
    n = len(s)
    rules = {}  # key: number, value: greater numbers set
    for i in range(n - 1):
        num1 = s[i]
        num2 = s[i + 1]
        if len(num1) != len(num2) or num1 == num2:
            continue
        j = 0
        while num1[j] == num2[j]:
            j += 1
        if num1[j] not in rules:
            rules[num1[j]] = set()
        rules[num1[j]].add(num2[j])

    print(rules)

    return summarize_rules(rules)


def summarize_rules(rules):
    for small_number in list(rules):
        large_numbers = rules[small_number]
        success = rules_helper(set([small_number]), set(large_numbers), rules)
    return rules, success


def rules_helper(smaller_numbers_set, larger_numbers_set, rules):
    print("A", smaller_numbers_set, larger_numbers_set)
    print("B", rules)
    new_larger_numbers_set = set()
    for number in larger_numbers_set:
        if number in rules:
            new_larger_numbers_set |= rules[number]
    if len(new_larger_numbers_set) > 0:
        for number in smaller_numbers_set:
            if number not in rules:
                rules[number] = set()
            rules[number] |= new_larger_numbers_set
            if number in rules[number]:
                return False
        return rules_helper(smaller_numbers_set | larger_numbers_set, new_larger_numbers_set, rules)
    return True


def get_larger_number_based_on_sorted_list(s, n1, n2, verbose=True):
    """Returns n1, n2, equal or unknown."""
    # convert everythin to string
    n1, n2 = str(n1), str(n2)
    for i in range(len(s)):
        s[i] = str(s[i])

    if verbose:
        print("LIST:  ", s)
        print("N1:    ", n1)
        print("N2:    ", n2)

    # first simple checks, make sure numbers are different and we can not guess by counting digits
    if len(n1) > len(n2):
        if verbose:
            print("RESULT: n1")
        return "n1"
    elif len(n1) < len(n2):
        if verbose:
            print("RESULT: n2")
        return "n2"
    elif n1 == n2:
        if verbose:
            print("RESULT: equal")
        return "equal"

    # we compare 2 different numbers of same length, we need to compute rules
    rules, success = get_rules_sorted_list(s)
    if not success:
        print("RESULT: error")
    if verbose:
        print("RULES: ", rules)

    # using rules, guess larger number
    for d1, d2 in zip(n1, n2):
        if d1 == d2:
            continue
        if d1 in rules and d2 in rules[d1]:
            if verbose:
                print("RESULT: n2")
            return "n2"
        elif d2 in rules and d1 in rules[d2]:
            if verbose:
                print("RESULT: n1")
            return "n1"
        if verbose:
            print("RESULT: unknown")
        return "unknown"



if __name__ == "__main__":
    s = ["8", "6", "2", "94", "39", "57", "56", "60", "467", "072", "333", "299"]
    get_larger_number_based_on_sorted_list(s, 41, 23)
    get_larger_number_based_on_sorted_list(s, 107, 105)
    get_larger_number_based_on_sorted_list(s, 1, 0)
    get_larger_number_based_on_sorted_list(s, 1, 1)
    get_larger_number_based_on_sorted_list(s, 1, 2)
    get_larger_number_based_on_sorted_list(s, 1, 3)
    get_larger_number_based_on_sorted_list(s, 1, 4)
    get_larger_number_based_on_sorted_list(s, 1, 5)
    get_larger_number_based_on_sorted_list(s, 1, 6)
    get_larger_number_based_on_sorted_list(s, 1, 7)
    get_larger_number_based_on_sorted_list(s, 1, 8)
    get_larger_number_based_on_sorted_list(s, 1, 9)
