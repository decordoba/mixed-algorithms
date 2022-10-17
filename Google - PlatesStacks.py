"""
Source: Winning Google Kickstart round A 2020

I changed the logic a bit so every stack can have different lengths.

Summary:
    There is group of plates with n stacks, each stack has k plates, each plate has a positive beauty value.
    We take p plates, but we can only take from the top, and we want to maximize the beauty in those k plates.
"""


def get_best_plates(plates, num_plates, offsets=None, ht=None):
    if offsets is None:
        offsets = tuple(len(plate) - 1 for plate in plates)
    if ht is None:
        ht = {}
    if num_plates == 0:
        return 0, []
    best_beauty = 0
    best_pos = []
    for i, (stack, offset) in enumerate(zip(plates, offsets)):
        if offset < 0:
            continue
        new_offsets = offsets[:i] + (offset - 1,) + offsets[i + 1:]
        if new_offsets in ht:
            beauty, pos = ht[new_offsets]
        else:
            beauty, pos = get_best_plates(plates, num_plates - 1, offsets=new_offsets, ht=ht)
            ht[new_offsets] = beauty, pos
        beauty = stack[offset] + beauty
        if beauty > best_beauty:
            best_beauty = beauty
            best_pos = pos + [i]
    return best_beauty, best_pos


def main(verbose=True):
    plates = [  # stacks of plates, every subarray is a plate stack
        [7, 1, 3, 4, 2, 5],
        [4, 2, 3, 4, 5],
        [10, 1],
        [1, 6, 2, 9]
    ]
    n = len(plates)  # number of stacks
    p = 7
    print("Plates:", plates)
    print("Plates to take:", p)
    beauty, path = get_best_plates(plates, p)
    print("Beauty:", beauty)
    print("Path:", path)
    plates_indices = list(len(plate) - 1 for plate in plates)
    taken = []
    for idx in path:
        taken += [plates[idx][plates_indices[idx]]]
        plates_indices[idx] -= 1
    print("Plates taken:", taken)


if __name__ == "__main__":
    main()
