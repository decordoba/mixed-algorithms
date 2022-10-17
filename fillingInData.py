"""
This comes from a surprisingly difficult test problem where there seems to be no correct answer.

The original problem says this:
A time series of daily readings of mercury levels in a river is provided to you.
In each test case, the day's highest level is missing for certain days.
By analyzing the data, try to identify the missing mercury levels for those days.
Each row of data contains two tab-separated values: a time-stamp and the day's highest reading.

There are exactly twenty rows marked missing in each input file.
The missing values are marked as "Missing_1", "Missing_2", ..., "Missing_20".
These missing records have been randomly dispersed in the rows of data.

Sample Input:
250
1/3/2012 16:00:00   Missing_1
1/4/2012 16:00:00   27.47
1/5/2012 16:00:00   27.728
1/6/2012 16:00:00   28.19
1/9/2012 16:00:00   28.1
1/10/2012 16:00:00  28.15
....
....
....
12/13/2012 16:00:00 27.52
12/14/2012 16:00:00 Missing_19
12/17/2012 16:00:00 27.215
12/18/2012 16:00:00 27.63
12/19/2012 16:00:00 27.73
12/20/2012 16:00:00 Missing_20
12/21/2012 16:00:00 27.49
12/24/2012 13:00:00 27.25
12/26/2012 16:00:00 27.2
12/27/2012 16:00:00 27.09
12/28/2012 16:00:00 26.9
12/31/2012 16:00:00 26.77

Sample Output:
26.96
31.98
32.69
32.41
32.32
30.5
29.18
30.8
30.46
30.63
30.96
30.4
28.2
28.2
27.3
27.1666
27.58
26.82
27.13
27.68

We will compute the mean of the magnitude of the percentage difference by comparing
your expected answers with the actual mercury level high for each of the missing records.
For all missing values we calculate:
    d = Summation of abs((expected_value[i] - computed_value[i]) / expected_value[i]) x 100
Then we take the average of d:
    d = d / (number of missing values)
Your final score on a scale of 100 will be:
    50 x max(2 - d, 0)
That is, if the mean value of 'd' exceeds 2% (your predictions are off by 2% or more on average), you will score a zero.
If your predictions are all right on target, you will score 100.
If your program throws an error (or an incorrect output format) for a single test case, the overall score assigned will be zero.

I have made a modification of this problem to allow any number of missing/incorrect values, and not evenly spaced times, and to plot estimations.
"""

from datetime import datetime, timedelta
from matplotlib import pyplot as plt
import math
import random


def plot_line(y_pts, x_pts, style="o", color="", fig_num=0, clf=False, show=True):
    fig = plt.figure(fig_num)
    if clf:
        fig.clf()
    plt.plot(x_pts, y_pts, color + style)
    plt.draw()
    if show:
        plt.show()


def estimate_missing_values(readings, plot=True):
    """Readings is an ordered list of data points (time, value) where some values are wrong (not a number).
    Fill the values with an estimation based on the known values to the left and right of the missing dots.
    If the missing dot is at the beginning or end, use the closest known dots before/after them.
    """
    times = []
    values = []
    missing_pos = []
    missing_times = []
    number_value = None
    for i, row in enumerate(readings.split("\n")):
        time, value = row.split("\t")
        times.append(datetime.strptime(time, '%Y-%m-%d %H:%M:%S'))
        try:
            number_value = float(value)
            values.append(number_value)
        except ValueError:
            values.append(None)
            missing_pos.append(i)
            missing_times.append(times[-1])
    if len(missing_pos) + 1 >= len(values):
        estimated_values = [number_value] * len(missing_pos)
    else:
        estimated_values = []
        for pos in missing_pos:
            prev_pos = pos - 1
            prev_val = None
            prev_time = None
            while prev_pos >= 0 and prev_val is None:
                prev_val = values[prev_pos]
                prev_time = times[prev_pos]
                prev_pos -= 1
            next_pos = pos + 1
            next_val = None
            next_time = None
            while next_pos < len(values) and next_val is None:
                next_val = values[next_pos]
                next_time = times[next_pos]
                next_pos += 1
            if prev_val is None:
                while next_pos < len(values) and prev_val is None:
                    prev_val = values[next_pos]
                    prev_time = times[next_pos]
                    next_pos += 1
            elif next_val is None:
                while prev_pos >= 0 and next_val is None:
                    next_val = values[prev_pos]
                    next_time = times[prev_pos]
                    prev_pos -= 1
            slope = (next_val - prev_val) / (next_time - prev_time).total_seconds()
            val = prev_val + slope * (times[pos] - prev_time).total_seconds()
            estimated_values.append(val)
    if plot:
        print(values, times)
        plot_line(values, times, style="o-", color="b", show=False)
        print(estimated_values, missing_times)
        plot_line(estimated_values, missing_times, style="o", color="r")
    return estimated_values


if __name__ == "__main__":
    inp = "\n".join([
        "2012-1-1 16:00:00	X",
        "2012-1-2 16:00:00	26.96",
        "2012-1-3 16:00:00	26.96",
        "2012-1-4 16:00:00	27.47",
        "2012-1-5 16:00:00	27.728",
        "2012-1-6 16:00:00	28.19",
        "2012-1-9 16:00:00	28.1",
        "2012-1-10 16:00:00	X",
        "2012-1-11 16:00:00	27.98",
        "2012-1-12 16:00:00	28.02",
        "2012-1-13 16:00:00	X",
        "2012-1-14 16:00:00	X",
        "2012-1-15 16:00:00	29.0",
        "2012-1-16 16:00:00	X",
        "2012-1-17 16:00:00	28.65",
        "2012-1-18 16:00:00	28.4",
        "2012-1-19 16:00:00	28.435",
        "2012-1-20 16:00:00	29.14",
        "2012-1-21 16:00:00	X",
    ])
    estimate_missing_values(inp, plot=True)

    times = [datetime(1999, 4, 5)]
    values = [0]
    total_offset = 0
    for i in range(100):
        offset = 6 + random.random() * 42
        total_offset += offset
        times.append(times[-1] + timedelta(hours=offset))
        values.append(math.sin(total_offset * math.pi / 24 / 7))
    rows = [str(time).split(".")[0] + "\t" + (str(value) if random.random() >= 0.2 else "X") for time, value in zip(times, values)]
    inp = "\n".join(rows)
    estimate_missing_values(inp, plot=True)
