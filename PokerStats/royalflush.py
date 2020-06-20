import more_itertools as mit


def royal_flush(num, suits):
    def get_key(item):
        return item[0]

    zipped = [list(x) for x in zip(num, suits)]
    zipped_sorted = sorted(zipped, key=get_key)

    num_lst = []
    for lst in zipped_sorted:
        num_lst.append(lst[0])
    sorted_num = [list(group) for group in mit.consecutive_groups(num_lst)]
    for consecutive_list in sorted_num:
        if len(consecutive_list) >= 5 and consecutive_list[-1] == 14:
            index1 = num_lst.index(consecutive_list[0])
            index2 = num_lst.index(consecutive_list[-1])
            new_zipped_sorted = zipped_sorted[index1:index2 + 1]
            suit = []
            for lst in new_zipped_sorted:
                suit.append(lst[1])
            suit = list(dict.fromkeys(suit))
            if len(suit) == 1:
                return 10
    if TypeError:
        return 0


# Testing
'''
n = [10, 6, 11, 3, 12, 14, 13]
l = ['C', 'C', 'C', 'C', 'C', 'C', 'C']
print(royal_flush(n, l))
'''

