import more_itertools as mit


def remove_values(the_list, val):
    return [value for value in the_list if value != val]


def straight_flush(num, suits):
    def get_key(item):
        return item[0]

    zipped = [list(x) for x in zip(num, suits)]
    zipped_sorted = sorted(zipped, key=get_key)

    num_lst = []
    for lst in zipped_sorted:
        num_lst.append(lst[0])
    sorted_num = [list(group) for group in mit.consecutive_groups(num_lst)]
    for consecutive_list in sorted_num:
        if len(consecutive_list) < 5:
            continue
        if len(consecutive_list) >= 5:
            index1 = num_lst.index(consecutive_list[0])
            index2 = num_lst.index(consecutive_list[-1])
        new_zipped_sorted = zipped_sorted[index1:index2 + 1]
        highest = new_zipped_sorted[-1]
    return highest[0]


def quads(nums):
    list_of_dup = []
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            duplicate_num = nums[i]
            list_of_dup.append(duplicate_num)
    for num in list_of_dup:
        count = nums.count(num)
        if count == 4:
            return num


def full_house(nums):
    list_of_dup = []
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            duplicate_num = nums[i]
            list_of_dup.append(duplicate_num)
    for num in list_of_dup:
        count = nums.count(num)
        if count == 3:
            list_of_dup.sort()
            new = remove_values(list_of_dup, num)
            return num, new[0]


def flush(num, suits):
    clubs = suits.count('C')
    diamonds = suits.count('D')
    hearts = suits.count('H')
    spades = suits.count('S')
    if clubs >= 5:
        suit = 'C'
    elif diamonds >= 5:
        suit = 'D'
    elif hearts >= 5:
        suit = 'H'
    elif spades >= 5:
        suit = 'S'

    def get_key(item):
        return item[0]

    zipped = [list(x) for x in zip(num, suits)]
    zipped_sorted = sorted(zipped, key=get_key)
    highest = []
    for lst in zipped_sorted:
        if lst[1] == suit:
            highest.append(lst[0])
    return max(highest)


def straight(nums):
    no_dups_sf = list(dict.fromkeys(nums))
    sorted_num = [list(group) for group in mit.consecutive_groups(no_dups_sf)]
    for lst in sorted_num:
        if len(lst) >= 5:
            return lst[-1]
        if TypeError:
            return 0


def trips(nums):
    lst = nums
    list_of_dup = []
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            duplicate_num = nums[i]
            list_of_dup.append(duplicate_num)
    for num in list_of_dup:
        count = nums.count(num)
        if count == 3:
            new = remove_values(lst, num)
            new.sort()
            return num, new[-2:]


def two_pair(nums):
    lst = nums
    list_of_dup = []
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            duplicate_num = nums[i]
            list_of_dup.append(duplicate_num)
    no_dup = list(dict.fromkeys(list_of_dup))
    no_dup.sort()
    x = remove_values(lst, no_dup[-1])
    y = remove_values(x, no_dup[-2])
    return max(no_dup), no_dup[-2], y[-1]


def one_pair(nums):
    lst = nums
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            new_lst = remove_values(lst, nums[i])
            return nums[i], new_lst[0:3]


def high_card(nums):
    return max(nums)


