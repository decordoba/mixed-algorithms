#!/usr/bin/env python
# Works in python2 and python3

"""
Hash table implementation without using a dictionary
"""


class hashTable(object):
    def __init__(self, number_buckets=100):
        self.number_buckets = number_buckets
        self.ht = [[] for _ in range(self.number_buckets)]
        self.k = []

    def get_bucket_number(self, key):
        return hash(key) % self.number_buckets

    def add(self, key, value):
        bucket = self.get_bucket_number(key)
        key_found = False
        for i, (other_key, _) in enumerate(self.ht[bucket]):
            if other_key == key:
                self.ht[bucket][i] = (key, value)
                key_found = True
                break
        if not key_found:
            self.ht[bucket].append((key, value))
            self.k.append(key)

    def get(self, key):
        bucket = self.get_bucket_number(key)
        for other_key, value in self.ht[bucket]:
            if other_key == key:
                return value
        raise KeyError("Key '{}' not found in hashTable".format(key))
        return None

    def remove(self, key):
        bucket = self.get_bucket_number(key)
        key_pos = None
        for i, (other_key, _) in enumerate(self.ht[bucket]):
            if other_key == key:
                key_pos = i
                break
        if key_pos is not None:
            self.ht[bucket] = self.ht[bucket][:key_pos] + self.ht[bucket][key_pos + 1:]

    def get_bucket(self, number):
        s = ""
        for key, value in self.ht[number]:
            s += "{}: {}, ".format(key, value)
        return "[" + s[:-2] + "]"

    def keys(self):
        return self.k

    def __len__(self):
        return len(self.k)

    def __setitem__(self, key, value):
        self.add(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __delitem__(self, key):
        return self.remove(key)

    def __str__(self):
        s = ""
        for bucket in self.ht:
            for key, value in bucket:
                s += "{}: {}, ".format(key, value)
        return "[" + s[:-2] + "]"


if __name__ == "__main__":
    num_buckets = 20
    ht1 = hashTable(number_buckets=num_buckets)

    print("Empty Hash Table:", ht1)

    ht1.add("km", 1000)
    ht1["m"] = 1
    ht1["hm"] = 100
    ht1.add("mm", 0.001)
    ht1["inch"] = 0.0254
    ht1.add("foot", 0.3048)
    ht1.add("mile", 1609.34)

    print("Full Hash Table:", ht1)
    print("Hash Table Length:", len(ht1))
    print("Keys: {}".format(ht1.keys()))

    print("Bucket Distribution:\n--------------------")
    for i in range(num_buckets):
        print("{:<3} {}".format(i, ht1.get_bucket(i)))
    print("--------------------")

    print("Access key {}: {}".format("inch", ht1.get("inch")))
    print("Access key {}: {}".format("mile", ht1["mile"]))
    ht1.remove("inch")
    print("Hash Table after removing element:", ht1)
    print("Accessing a removed element will result in a KeyError:")
    print("Access key {}: {}".format("inch", ht1.get("inch")))
