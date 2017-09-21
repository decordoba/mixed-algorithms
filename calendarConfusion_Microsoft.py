"""
Easier Challenge 3 from Microsoft Competition at WashU (9 min)

Calendar confusion | 1 point(s)

Danny Lasagna has finally made it; his pizza place is expanding from one local shop to a
multi-national chain all over the world. The online ordering system, however, is causing issues
because different countries use different formats for their dates. Your task is to write a program
that converts dates from one format to another.

Input definition

An input file for this problem will contain less than 1000 lines of space separated triples.
Each line will contain a date, its current format, and the desired output format.

Output definition

Your output should contain the same number of lines as the given input file. Each line should
contain the given input date in the desired output format.

Example input

2017-09-04 yyyy-mm-dd mm*yyyy*dd

Example output

09*2017*04
"""


if __name__ == "__main__":
    inp = """2017-09-04 yyyy-mm-dd mm*yyyy*dd"""

    for line in inp.split("\n"):
        original, original_format, new_format = line.split()
        y_idx = original_format.index("yyyy")
        m_idx = original_format.index("mm")
        d_idx = original_format.index("dd")

        year = original[y_idx : y_idx + 4]
        month = original[m_idx : m_idx + 2]
        day = original[d_idx : d_idx + 2]

        y_idx = new_format.index("yyyy")
        m_idx = new_format.index("mm")
        d_idx = new_format.index("dd")

        # Definitely not the most optimal way, but it works and can be coded fast
        new_format = list(new_format)
        for i in range(4):
            new_format[y_idx + i] = year[i]
        for i in range(2):
            new_format[m_idx + i] = month[i]
            new_format[d_idx + i] = day[i]
        new_format = "".join(new_format)

        print(new_format)