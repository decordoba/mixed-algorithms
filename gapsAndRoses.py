"""
I had to solve this algorithm for a Google interview. The worst part of
it was that it had to be solved in O(NlogN) time, and although I solved
the challenge in time, I did not have time to implement the binary search,
so my original algorithm would run in O(N^2).

The problem consists on counting the length of the gaps between non bloomed
rose bushes, knowing that at the beginning (t=0) all the N rose bushes have
not bloomed yet, and that every iteration t, one and only one of them blooms.
We have to return the iteration where an exact gap of non blommed roses exists.

We receive 2 inputs: an unsorted array of N numbers, where all the
integers from 1 to N will appear only once; and  an int representing
the gap we are looking for. We will have to return the iteration in
which this gap appears for the first time.

Basically, we get:
    ([2, 1, 3, 5, 4], 2)
therefore, we see:
    [0, 1, 0, 0, 0]   * Rose 2 blooms (there is 1 gap len1 & 1 gap len3)
    [1, 1, 0, 0, 0]   * Rose 1 blooms (there is 1 gap len3)
    [1, 1, 1, 0, 0]   * Rose 3 blooms (there is 1 gap len2)
    [1, 1, 1, 0, 1]   * Rose 5 blooms (there is 1 gap len1)
    [1, 1, 1, 1, 1]   * Rose 4 blooms (there is no gap)
so we should return:
    3

Explanation: Because the 2nd input is a 2, we have to return 3,
because t=3 is the first time that we see a gap of only 2 zeros
[1, 1, 1, 0, 0]. If the required gap never happens, we mus return
-1 (for example, for inputs ([2,4,1,3,5], 2))

Example 2:
([5, 6, 2, 4, 1, 3], 3) returns 3

Minimum Requirements:
    * time complexity: O(N*log(N))
    * space complexity: O(N)
"""


def solution(P, K):
    # Return iteration in which we first find a gap of size K
    n = len(P)
    ok_land = []
    for i, p in enumerate(P):
        # returns 1st rose before and after, and idx after_rose
        bef, aft, idx = find_idx(p, ok_land, max_num=n)
        diff_bef = p - bef - 1
        diff_aft = aft - p - 1
        if diff_bef == K or diff_aft == K:
            return i + 1
        # We can optimize the search if we do not add roses for small gaps
        if diff_bef + diff_aft >= K:
            ok_land = ok_land[:idx] + [p] + ok_land[idx:]
    return -1


def find_idx(el, array, max_num):
    # Binary search (complexity O(log(N))), we return the number
    # before and after 'el' in 'array', and the index of the larger
    # number in 'array'. For this to work, 'el' should not be
    # in 'array', and 'array' must be sorted. For example, el=5,
    # array=[1,2,4,9,11] returns (4, 9, 3); el=2, array=[4,6,7]
    # returns (0, 4, 0); el=10, array=[1,5,8,9], max_num=12
    # returns (9, 13, 4)
    min_pos = 0
    max_pos = len(array)
    pos = 0
    # Search pos where numbers go from smaller than el to larger than el
    while max_pos - min_pos > 1:
        # Assume el not in array => array[pos] can only be > or < el, not =
        pos = (max_pos + min_pos) // 2
        if array[pos] > el:
            max_pos = pos
        else:
            min_pos = pos
    # These if-else deal with some corner cases in the search
    if len(array) == 0:
        prev, nex, idx = 0, max_num + 1, 0
    elif array[pos] > el:
        if pos > 0:
            if array[pos - 1] < el:
                prev = array[pos - 1]
                nex = array[pos]
                idx = pos
            else:
                prev = 0
                nex = array[pos - 1]
                idx = pos - 1
        else:
            prev = 0
            nex = array[pos]
            idx = pos
    else:
        if pos < len(array) - 1:
            if array[pos + 1] > el:
                prev = array[pos]
                nex = array[pos + 1]
                idx = pos + 1
            else:
                prev = array[pos + 1]
                nex = max_num + 1
                idx = len(array)
        else:
            prev = array[pos]
            nex = max_num + 1
            idx = len(array)
    return (prev, nex, idx)


if __name__ == "__main__":
    # Some test cases
    print(solution([2,4,1,3], 1))  # 1
    print(solution([2,4,1,3,5], 2))  # -1
    print(solution([2,1,4,3,5,6], 2))  # 3
    print(solution([1,4,2,3,5], 2))  # 2
    print(solution([1,7,5,3,20,11,9,12,8,15,6,17,2,4,13,18,10,19,14,16], 1))  # 3
    print(solution([1,7,5,3,20,11,9,12,8,15,6,17,2,4,13,18,10,19,14,16], 2))  # 10
    print(solution([1,7,5,3,20,11,9,12,8,15,6,17,2,4,13,18,10,19,14,16], 3))  # 3
    print(solution([1,7,5,3,20,11,9,12,8,15,6,17,2,4,13,18,10,19,14,16], 4))  # 10
    print(solution([1,7,5,3,20,11,9,12,8,15,6,17,2,4,13,18,10,19,14,16], 5))  # 2
    print(solution([1,7,5,3,20,11,9,12,8,15,6,17,2,4,13,18,10,19,14,16], 6))  # -1
    print(solution([1,7,5,3,20,11,9,12,8,15,6,17,2,4,13,18,10,19,14,16], 7))  # 8
    print(solution([1,7,5,3,20,11,9,12,8,15,6,17,2,4,13,18,10,19,14,16], 8))  # 6
    print(solution([1,7,5,3,20,11,9,12,8,15,6,17,2,4,13,18,10,19,14,16], 9))  # -1
    print(solution([1,7,5,3,20,11,9,12,8,15,6,17,2,4,13,18,10,19,14,16], 10))  # -1
    print(solution([1,7,5,3,20,11,9,12,8,15,6,17,2,4,13,18,10,19,14,16], 11))  # -1
    print(solution([1,7,5,3,20,11,9,12,8,15,6,17,2,4,13,18,10,19,14,16], 12))  # 5
    print(solution([1,7,5,3,20,11,9,12,8,15,6,17,2,4,13,18,10,19,14,16], 13))  # 2
