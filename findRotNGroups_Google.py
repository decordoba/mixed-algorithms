#!/usr/bin/env python
# Works in python2 and python3

"""
Algorithm for a phone interview at Google (it went well, I ended up getting an onsite
final interview in Mountain View). It was kind of tough to understand how to do it in
the time given (30 min approx), but not impossible. The key was realizing that it was
not necessary to create a rot-N function.

Any word can be rotated an N number of times, which means that all letters of the word
(lower-case only) are shifted to the right.
Also, letters that get to the end of the alphabet start over.

Examples:
* ROT-13 (rotate it by 13 letters)
    "abc" -> "nop"
    "hello" -> "uryyb"
* ROT-1 (rotate it by 1 letters)
    "az" -> "ba"

Write a function that takes a collection of strings (containing only lower-case letters),
determines and returns which are ROT-n equivalents of each other.

Example:
Given as args:
    ["abbc", "bccd", "cat", "zaab", "yell", "bzs", "catch"]
the function returns:
    abbc, bccd, zaab
    cat, bzs
"""

LETTERS_ALPHABET = 26


def match_string(str_list):
    # From a list of lower-case words, returns an array of ROT-N groups.
    # Example: ["ac", "bd", "mn", "zb", "xy"] --> [["ac", "bd", "zb"], ["mn", "xy"]]
    ht = {}
    for s in str_list:
        n = get_chars_sep(s)
        if n in ht:
            ht[n].append(s)
        else:
            ht[n] = [s]
    r = []
    for k in ht.keys():
        if len(ht[k]) > 1:
            r.append(ht[k])
    return r


def get_chars_sep(s):
    # Get separation between letters in a word.
    # Example: "abcmzb" --> (1, 1, 10, 13, 2)
    n = len(s) - 1
    r = []
    for i in range(n):
        r.append(((ord(s[i + 1]) - ord(s[i])) % LETTERS_ALPHABET))
    return tuple(r)


def rot_N(s, n):
    # Rotate string n characters
    # This function is not necessary to solve the problem, but it is fun to code!
    new_s = ""
    maxv = ord("z")
    n = n % LETTERS_ALPHABET
    for c in s:
        val = ord(c) + n
        if val > maxv:
            val -= LETTERS_ALPHABET
        new_s += chr(val)
    return new_s


def test(inp, outp, first=False):
    # Fail if match_string function does not work. Else, print result.
    result = match_string(inp)
    if len(outp) != len(result):
        assert False, "{} and {} have different lengths".format(result, outp)  # Fail
    for r in result:
        i = 0
        while i < len(outp):
            if r[0] in outp[i]:
                break
            i += 1
        if i >= len(outp):
            assert False, "The first element of {} was not found in {}".format(r, outp)  # Fail
        if len(r) != len(outp[i]):
            assert False, "{} does not match {}".format(r, outp[i])  # Fail
        for word in outp[i]:
            if word not in r:
                assert False, "{} does not match {}".format(r, outp[i])  # Fail
        # This seems redundant, but it makes sure no corner cases can succeed when they shouldn't
        for word in r:
            if word not in outp[i]:
                assert False, "{} does not match {}".format(r, outp[i])  # Fail
    if first:
        print("--------------------------")
    print("INPUT:")
    print("  '" + "'\n  '".join(inp) + "'")
    print("OUTPUT:")
    for r in result:
        print("  '" + "' '".join(r) + "'")
    print("--------------------------")


if __name__ == "__main__":
    test(["abbc", "bccd", "cat", "zaab", "yell", "bzs", "catch"],
         [["abbc", "bccd", "zaab"], ["cat", "bzs"]], first=True)
    test([], [])
    test(["aa", "ba"], [])
    test(["", ""], [["", ""]])
    test(["a", "b"], [["a", "b"]])
    test(["aa", "ba"], [])
    test(["aa", "aa"], [["aa", "aa"]])
    test(["ac", "bd", "mn"], [["ac", "bd"]])
    test(["ac", "bd", "mn", "zb", "xy"], [["ac", "bd", "zb"], ["xy", "mn"]])
    test(["daniel", "bd", "mn"], [])
    test(["jtu", "xov", "hqx", "aof", "xyr", "yit", "vkt", "efw", "qus", "rnn", "lyw", "vwi",
          "qsv", "zwy", "ool", "nby", "zmo", "huc", "jqt", "frk", "mlk", "dbm", "vuc", "sou",
          "ghk", "obt", "wzs", "sfa", "abl", "ljm", "ddn", "wjq", "ims", "ybd", "lav", "uao",
          "qyr", "hco", "gbp", "eot", "qwe", "wxn", "vli", "apd", "zpq", "uoe", "ktl", "hnn",
          "zsf", "mvv", "rbh", "imd", "pce", "iak", "iqq", "vtb", "olk", "jwk", "loq", "gwh",
          "edz", "aoz", "cey", "oeq", "rrq", "izn", "qpc", "csi", "bxn", "kuf", "xkz", "egc",
          "zmn", "vqv", "pbc", "wwm", "ihw", "jsb", "jyd", "ein", "fvd", "ies", "crz", "xxn",
          "bgj", "por", "pgv", "ckb", "qur", "gbo", "pxd", "njx", "onc", "skm", "zmq", "get",
          "jcf", "gcu", "fbt", "ijs", "etd", "kft", "cdx", "pxg", "ifp", "mqq", "jdr", "kqr",
          "xau", "mrf", "kuc", "ywl", "aaq", "uyj", "ztq", "yux", "kpf", "fik", "rpw", "csf",
          "ccs", "quu", "lwo", "dan", "ppp"],
         [['quu', 'mqq'], ['ihw', 'onc'], ['get', 'ywl'], ['loq', 'ybd', 'fik'], ['gbp', 'kft'],
          ['ies', 'njx'], ['zmo', 'pce'], ['gcu', 'fbt'], ['wwm', 'xxn', 'aaq', 'ccs'],
          ['yit', 'kuf']])
