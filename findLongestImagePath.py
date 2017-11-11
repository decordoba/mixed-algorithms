#!/usr/bin/env python2

"""
I had to face this challenge in one of my interviews.
We are given a listing of directories and files in a file system. Each directory has a name,
which is a non-empty string without any dot '.' character. The name of all files contain at
least one dot '.'. Each entry is listed in a new line. Every directory is followed by the listing
of its contents indented by one space character. The root is not indented. The absolute path of a
directory is a string containing the directories from the root. Example:
dir1
 dir11
 dir12
  dir121
  who said folders couldn't include spaces
   file1.txt
   dir1211
    dir12111
    xxx.png
  pic2.jpeg
dir2
 file2.gif
file1.png

From here, we have to return the length of the longest absolute path of an image (files ending in
.jpeg, .gif or .png), not counting the image name. In our example, the longest path for an image
is: "/dir1/dir12/who said folders couldn't include spaces/dir1211/xxx.png", so we would return
len("/dir1/dir12/who said folders couldn't include spaces/dir1211") = 60.
"""

from basic import *  # Find basic.py in https://github.com/decordoba/basic-python


def findLongestImagePath(listing):
    nesting = -1
    current_path = []
    max_length = 0
    for line in listing.split("\n"):
        # Skip empty lines
        if len(line) == 0:
            continue
        # Count spaces to know depth of the folder / file
        spaces = countSpaces(line)
        # Remove spaces left and right of the folder / file name
        line = line.strip()
        # Adjust current_path length to match the folder / file depth
        while spaces > nesting:
            current_path.append(0)
            nesting += 1
        while spaces < nesting:
            current_path.pop()
            nesting -= 1
        # Set last element to 0 (overwrite previous value)
        current_path[-1] = 0

        # If we are looking at a folder
        if '.' not in line:
            # Save length folder
            current_path[-1] = len(line) + 1  # We add 1 because of the /
        # If we are looking at a file
        else:
            extension = line[line.rfind("."):]
            # If we are looking at an image
            if extension == ".png" or extension == ".jpeg" or extension == ".gif":
                # Save max length, which is sum of lengths of all paths
                max_length = max(max_length, sum(current_path))

    return max_length


def countSpaces(s):
    # Count spaces from beginning of str to first non-space char
    counter = 0
    for c in s:
        if c != " ":
            return counter
        counter += 1
    return len(s)


def findLongestImagePath2(listing):
    """
    Another way of doing this with a hash table, simpler and shorter, I thought about it later...
    Still, it is pretty similar.
    """
    max_length = 0
    current_path = {0: 0}

    for line in listing.split("\n"):
        # Skip empty lines
        if len(line) == 0:
            continue
        # Count spaces to know depth of the folder / file
        dirdepth = countSpaces(line)
        # Remove spaces left and right of the folder / file name
        line = line.strip()

        # If we are looking at a folder
        if '.' not in line:
            # Save total length of path for current folder
            current_path[dirdepth+1] = current_path[dirdepth] + len(line) + 1
        # If we are looking at a file
        else:
            extension = line[line.rfind("."):]
            # If we are looking at an image
            if extension == ".png" or extension == ".jpeg" or extension == ".gif":
                # Save max length, if our path length is greater than the one stored
                max_length = max(max_length, current_path[dirdepth])

    return max_length


if __name__ == "__main__":
    # Sample input
    inp = """
dir1
 dir11
 dir12
  dir121
  who said folders couldn't include spaces
   file1.txt
   dir1211
    dir12111
    nudes;P.png
   tmp.gif
  pic2.jpegg
dir2
 file2.gif
file1.png
"""
    # Read file or use sample input
    listing = readFileArgument(input=inp)
    # Test method 1
    print(findLongestImagePath(listing))
    # Test method 2
    print(findLongestImagePath2(listing))
