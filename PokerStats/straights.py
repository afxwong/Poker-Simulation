import more_itertools as mit


def straight(nums):
    no_dups = list(dict.fromkeys(nums))
    sorted_num = [list(group) for group in mit.consecutive_groups(no_dups)]
    for lst in sorted_num:
        if len(lst) >= 5:
            return 5
        else:
            return 0


# Testing
'''
n = [1, 2, 2, 3, 4, 5, 11]
straight(n)
'''
