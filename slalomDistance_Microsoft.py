#!/usr/bin/env python
# Works in python2 and python3

"""
Harder Challenge 2 from Microsoft Competition at WashU (several days, I made an algorithm that
solved many cases in 1:30h, but it took me a while to figure out the best solution that always
works)

Slalom Distance | 3 point(s)

You've decided to start slalom skiing. In slalom skiing, you start at some location and must ski
through a series of gates. Each gate is defined by two flags that you must ski through. For
simplicity, the gates will all be vertically aligned to the y-axis, meaning that both points
defining each gate will share the same x-coordinate. You want to be the best, so you are
going to write a program to find the fastest path through a series of gates.

Given a series of slalom gates, your program should find the shortest path through those gates.

Input definition

The first line of an input file for this problem will be an integer T, the number of test cases.
For each test case, the first line will contain two integers, N and S; they respectively represent
the number of slalom gates and your starting position's y-coordinate. The next N lines of each
test case contain two integers, y1 and y2, describing the y-coordinates of the slalom gates, in
order of increasing x-coordinate. Your starting x-coordinate is always 0 and consecutive gates are
at consecutive x-coordinates (i.e. x=1,2,3...N).

The following bounds shall apply:

1 ≤ T ≤ 50
2 ≤ N ≤ 50
0 ≤ S, y1 ≤ 50
y1 < y2
0 < y2 ≤ 60

Output definition

Your output should contain T lines, one for each given test case. For each test case, your output
should be the length of the shortest path from your starting position through all the slalom gates,
rounded to 4 decimal places.

Example input

2
3 2
1 4
3 6
1 2
6 2
1 2
2 3
3 4
2 3
1 2
2 3

Example output

3.6503
6.4721
"""

import matplotlib.pyplot as plt
from math import sqrt


def plot_line(y_pts, x_pts, style="o", color="", fig_num=0, clf=False, show=True):
    # Plot line
    fig = plt.figure(fig_num)
    if clf:
        fig.clf()
    plt.plot(x_pts, y_pts, color + style)
    plt.draw()
    if show:
        plt.show()


def get_line(x1, y1, x2, y2):
    # Get line function [m, n] from two points (y = m*x + n)
    m = (y1 - y2) / (x1 - x2)
    n = y1 - m * x1
    return m, n


def get_distance(pos1, pos2):
    # Calculate dist between two points
    x1, y1 = pos1
    x2, y2 = pos2
    return sqrt(pow(x1 - x2, 2.0) + pow(y1 - y2, 2.0))


def plot_gates(x0, y0, gates_list):
        # Plot gates using matplotlib
        pts_x = []
        pts_y1 = []
        pts_y2 = []
        num_gates = len(gates_list)
        plot_line([y0], [x0], color="r", clf=True, show=False)
        for i in range(num_gates):
            pts_x.append(i + 1)
            y1, y2 = gates_list[i]
            pts_y1.append(y1)
            pts_y2.append(y2)
            plot_line([y1, y2], [i + 1, i + 1], color="k", style="-", show=False)
        plot_line(pts_y1, pts_x, color="b")
        plot_line(pts_y2, pts_x, color="g")


def plot_gates_and_path(x0, y0, gates_list, best_path, lines_up=[], lines_down=[]):
    # Plot gates and path through gates. Can also plot lines_up and lines_down
    plot_gates(x0, y0, gates_list)
    for i in range(len(best_path) - 1):
        plot_line([best_path[i + 1][1]], [best_path[i + 1][0]], color="y", style="o")
        plot_line([best_path[i][1], best_path[i + 1][1]], [best_path[i][0], best_path[i + 1][0]],
                  color="c", style="-")
    for tx0, ty0, tx1, ty1, _1, _2 in lines_up:
        plot_line([ty1], [tx1], color="w", style="x")
        plot_line([ty0, ty1], [tx0, tx1], color="m", style="-")
    for tx0, ty0, tx1, ty1, _1, _2 in lines_down:
        plot_line([ty1], [tx1], color="c", style="x")
        plot_line([ty0, ty1], [tx0, tx1], color="r", style="-")


if __name__ == "__main__":
    inp = """9
13 1.5
3 10
14 16
0 2
0 3
0 5
0 8
0 12
-1 7
-1.5 9
4 10
1 16
3 15
0 16
18 1.5
0 2
0 3
0 5
0 8
0 12
-1 7
-1.5 9
3 10
14 16
0 2
0 3
0 5
0 8
0 12
-1 7
-1.5 9
3 10
14 16
3 2
1 4
3 6
1 2
6 2
1 2
2 3
3 4
2 3
1 2
2 3
4 15
50 57
17 31
3 20
33 43
11 15
50 57
17 31
3 20
33 43
41 51
8 13
26 31
14 22
29 39
14 22
28 15
6 15
23 29
7 17
46 56
33 40
3 12
33 42
22 32
20 30
28 36
26 32
35 45
9 17
19 29
15 20
41 49
4 14
25 31
50 57
17 27
3 9
33 43
41 51
8 13
26 31
14 22
29 39
14 22
28 15
6 15
23 29
7 17
46 56
33 40
3 12
33 42
22 32
20 30
28 36
26 32
35 45
9 17
19 29
15 20
41 49
4 14
25 31
50 57
17 27
3 9
33 43
41 51
8 13
26 31
14 22
29 39
14 22"""

    show_debug_plots = True
    plt.ion()
    lines = inp.split("\n")
    num_cases = int(lines[0])
    case_idx = 1
    for case in range(num_cases):
        # Get case variables
        num_gates, y0 = lines[case_idx].split()
        num_gates = int(num_gates)
        original_x0 = 0
        original_y0 = float(y0)

        # Get list gates
        gates_list = []
        for i in range(num_gates):
            y1, y2 = lines[case_idx + i + 1].split()
            y1, y2 = (float(y1), float(y2))
            if y1 > y2:
                y1, y2 = y2, y1
            gates_list.append((y1, y2))
        case_idx += num_gates + 1

        if show_debug_plots:
            plot_gates(original_x0, original_y0, gates_list)
            input("Press ENTER to continue")

        # Find shortest path to every gate
        x0, y0 = original_x0, original_y0
        best_path = [(x0, y0)]
        path_length = 0
        lines_up = []
        lines_down = []
        for i, (y1, y2) in enumerate(gates_list):
            # Get line (y = mx + n) from origin (x0, y0) to pts y1 and y2
            x = i + 1
            m1, n1 = get_line(x, y1, x0, y0)
            m2, n2 = get_line(x, y2, x0, y0)

            # Find shortest paths to south edge (y1) of current gate
            new_lines_down = []
            new_m1, new_n1 = m1, n1
            new_x0, new_y0 = x0, y0
            for prev_x0, prev_y0, prev_x, prev_y1, prev_m1, prev_n1 in lines_down:
                y1_proj = prev_m1 * x + prev_n1
                if y1_proj <= y1:
                    # discard old line and all lines after it, the new gate can be reached without
                    # worrying going through the old gate's edge
                    break
                else:
                    # We have to worry about two lines now: the old one and the new one
                    new_lines_down.append((prev_x0, prev_y0, prev_x, prev_y1, prev_m1, prev_n1))
                    new_x0, new_y0 = prev_x, prev_y1
                    new_m1, new_n1 = get_line(x, y1, prev_x, prev_y1)
            new_lines_down.append((new_x0, new_y0, x, y1, new_m1, new_n1))
            lines_down = new_lines_down

            # Find shortest paths to north edge (y2) current gate
            new_lines_up = []
            new_m2, new_n2 = m2, n2
            new_x0, new_y0 = x0, y0
            for prev_x0, prev_y0, prev_x, prev_y2, prev_m2, prev_n2 in lines_up:
                y2_proj = prev_m2 * x + prev_n2
                if y2_proj >= y2:
                    # discard old line and all lines after it, the new gate can be reached without
                    # worrying going through the old gate's edge
                    break
                else:
                    # We have to worry about two lines now: the old one and the new one
                    new_lines_up.append((prev_x0, prev_y0, prev_x, prev_y2, prev_m2, prev_n2))
                    new_x0, new_y0 = prev_x, prev_y2
                    new_m2, new_n2 = get_line(x, y2, prev_x, prev_y2)
            new_lines_up.append((new_x0, new_y0, x, y2, new_m2, new_n2))
            lines_up = new_lines_up

            # If the north and south path cross each other, the path collapses (there is only
            # one possible shortest path) for some of the lines_up and lines_down segments
            # Here we add the collapsed path to best_path, and fix lines_up and lines_down
            m_up = lines_up[0][4]
            m_down = lines_down[0][4]
            if m_up <= m_down:
                # The south path must follow the north path
                if len(lines_down) == 1:
                    old_x0, old_y0, old_x, old_y1, old_m1, old_n1 = lines_down[0]
                    for idx, (prev_x0, prev_y0, prev_x, prev_y2, prev_m2, prev_n2) in enumerate(lines_up):
                        if prev_m2 <= old_m1:
                            path_length += get_distance(best_path[-1], (prev_x, prev_y2))
                            best_path.append((prev_x, prev_y2))
                            old_m1, old_n1 = get_line(prev_x, prev_y2, old_x, old_y1)
                            old_x0, old_y0 = prev_x, prev_y2
                        else:
                            break
                    lines_down = [(old_x0, old_y0, old_x, old_y1, old_m1, old_n1)]
                    lines_up = lines_up[idx:]
                # The north path must follow the south path
                elif len(lines_up) == 1:
                    old_x0, old_y0, old_x, old_y2, old_m2, old_n2 = lines_up[0]
                    for idx, (prev_x0, prev_y0, prev_x, prev_y1, prev_m1, prev_n1) in enumerate(lines_down):
                        if old_m2 <= prev_m1:
                            path_length += get_distance(best_path[-1], (prev_x, prev_y1))
                            best_path.append((prev_x, prev_y1))
                            old_m2, old_n2 = get_line(prev_x, prev_y1, old_x, old_y2)
                            old_x0, old_y0 = prev_x, prev_y1
                        else:
                            break
                    lines_up = [(old_x0, old_y0, old_x, old_y2, old_m2, old_n2)]
                    lines_down = lines_down[idx:]
                # This case should never be reached
                else:
                    print("This should never happen! If it does, rethink the algorithm.")
                    raise Exception()
                x0 = old_x0
                y0 = old_y0

            if show_debug_plots:
                plot_gates_and_path(original_x0, original_y0, gates_list, best_path, lines_up,
                                    lines_down)
                input("Press ENTER to continue")

        # Solve last part of the path, where we want to reach the gate
        m1 = lines_down[0][4]
        m2 = lines_up[0][4]
        if m1 <= 0 and m2 >= 0:
            path_length += get_distance(best_path[-1], (x, y0))
            best_path.append((x, y0))
        elif m1 > 0:
            for _1, _2, new_x, new_y, new_m, _4 in lines_down:
                if new_m <= 0:
                    break
                path_length += get_distance(best_path[-1], (new_x, new_y))
                best_path.append((new_x, new_y))
            path_length += get_distance(best_path[-1], (new_x, best_path[-1][1]))
            best_path.append((x, best_path[-1][1]))
        else:
            for _1, _2, new_x, new_y, new_m, _4 in lines_up:
                if new_m >= 0:
                    break
                path_length += get_distance(best_path[-1], (new_x, new_y))
                best_path.append((new_x, new_y))
            path_length += get_distance(best_path[-1], (new_x, best_path[-1][1]))
            best_path.append((x, best_path[-1][1]))

        # Plot and print result
        plot_gates_and_path(original_x0, original_y0, gates_list, best_path)
        print("Path length: {}".format(round(path_length, 4)))
        input("Press ENTER to see the next case")
