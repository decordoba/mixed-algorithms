"""
Medium Challenge 3 from Microsoft Competition at WashU (20min)

Enhanced path | 2 point(s)

In the evolving world of command-line tools, the Windows team is always adding new features. On
top of the current shortcuts of “.” for the current folder and the “..” for the parent folder, in
this problem we'll consider two new features to a standard command line path:

The asterisk (*) will now represent the root folder.
A list of more than 2 dots (.) will represent more of the ancestry then just the parent. For each
additional dot, you should move up one additional folder. For example “...” would represent the
grandparent folder and “....” Would represent the great grandparent folder.
Given a path containing any of the current or new shortcuts, your program should normalize that
path to the shortest possible path that contains no shortcuts.

It is noted that for this problem, a set of characters that include shortcut characters but are not
the full string, shall be treated as a folder name. For example, a folder can be named ** or ..*,
and neither * nor . shall be interpreted as potential shortcuts in those cases since the former
contains two *s and the latter contains a combintation of shortcut characters that itself is not
a valid shortcut.

Input definition

An input file for this problem will contain multiple lines, each containing a single path. For
simplicity, all paths will be rooted with \ excluding the drive (i.e. c:).

Output definition

For each line of input, your output should be the normalized path. This path should contain no
shortcuts and be as short as possible.

Example input

\1
\1\2
\1\2\.
\1\2\..
\1\2\..\..
\1\2\...
\1\2\3\....
\1\2\3\4\.....\5\6\7
\1\..\..
\1\..\..\..\2\..\3
\1\\2
\1\2.3
\1\.2
\1\...2
\1\2.3.4.
\1\2...3.4.
\*
\1\*
\1\2\*
\1\*\2
\1\**\2
\1\2\3\.\4\5\..\...\*\2\3\4\....\5\6\.\.\7
\1.2\3*\.\4\5\..*\6\7\*.*
\..\...\1\2\3\*\4\5\6\7\8\9\10\11\12\13\......

Example output

\1
\1\2
\1\2
\1
\
\
\
\5\6\7
\
\3
\1\2
\1\2.3
\1\.2
\1\...2
\1\2.3.4.
\1\2...3.4.
\
\
\
\2
\1\**\2
\5\6\7
\1.2\3*\4\5\..*\6\7\*.*
\4\5\6\7\8
"""

if __name__ == "__main__":
    inp = r"""\1
\1\2
\1\2\.
\1\2\..
\1\2\..\..
\1\2\...
\1\2\3\....
\1\2\3\4\.....\5\6\7
\1\..\..
\1\..\..\..\2\..\3
\1\\2
\1\2.3
\1\.2
\1\...2
\1\2.3.4.
\1\2...3.4.
\*
\1\*
\1\2\*
\1\*\2
\1\**\2
\1\2\3\.\4\5\..\...\*\2\3\4\....\5\6\.\.\7
\1.2\3*\.\4\5\..*\6\7\*.*
\..\...\1\2\3\*\4\5\6\7\8\9\10\11\12\13\......"""

    for line in inp.split("\n"):
        tmp_path = line.split("\\")
        path = []
        for folder in tmp_path:
            if len(folder) <= 0:
                # Skip first \ character
                continue
            if folder == "*":
                # Flush all folders, go back to root
                path = []
            elif folder == ".":
                # "." Folder (ignore)
                pass
            elif folder[0] != ".":
                # Folder that does not start with a "."
                path.append(folder)
            elif "." * len(folder) == folder:
                # Folder with only dots (".")
                num_dels = len(folder) - 1
                while num_dels > 0 and len(path) > 0:
                    path.pop()
                    num_dels -= 1
            else:
                # Folder name that starts with "." but contains non-dot characters
                path.append(folder)
        print("\\" + "\\".join(path))
