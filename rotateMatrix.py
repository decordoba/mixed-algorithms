import math

"""
I've herd this was a 'hard' question in a Microsoft interview.
Rotate a matrix IN PLACE.
"""


def print_matrix(a):
    for aa in a:
        for aaa in aa:
            print("{:02d} ".format(aaa), end='')
        print()
    print()


def rotate_matrix(a, clockwise=True, verbose=False):
    # Rotate matrix in place
    depth = 0
    h = len(a)
    w = len(a[0])
    if w != h:
        print("Can't rotate, the matrix has to be a square!")
        return False
    if verbose:
        idx = 0
        print("Original matrix:")
        print_matrix(a)
    last = w - 1
    for depth in range(w // 2):
        for pos in range(depth, last-depth):
            t0, t1 = (pos, depth)
            b0, b1 = (last-pos, last-depth)
            if clockwise:
                r0, r1 = (last-depth, pos)
                l0, l1 = (depth, last-pos)
            else:
                r0, r1 = (depth, last-pos)
                l0, l1 = (last-depth, pos)
            tmp = a[t0][t1]
            a[t0][t1] = a[r0][r1]
            a[r0][r1] = a[b0][b1]
            a[b0][b1] = a[l0][l1]
            a[l0][l1] = tmp
            if verbose:
                idx += 1
                print("Matrix after {} steps:".format(idx))
                print_matrix(a)
    return True


if __name__ == "__main__":    
    m = [[1,2],
         [3,4]]

    m = [[1,2,3],
         [4,5,6],
         [7,8,9]]

    m = [[ 1, 2, 3, 4],
         [ 5, 6, 7, 8],
         [ 9,10,11,12],
         [13,14,15,16]]

    m = [[ 1, 2, 3, 4, 5],
         [ 6, 7, 8, 9,10],
         [11,12,13,14,15],
         [16,17,18,19,20],
         [21,22,23,24,25]]
         
    success = rotate_matrix(m, clockwise=False, verbose=True)
