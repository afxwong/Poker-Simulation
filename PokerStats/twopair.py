def two_pair(nums):
    list_of_dup = []
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            duplicate_num = nums[i]
            list_of_dup.append(duplicate_num)
    no_dup = list(dict.fromkeys(list_of_dup))
    if len(no_dup) >= 2:
        return 3
    else:
        return 0


# Testing
'''
n = [2, 2, 4, 4, 4, 14]
two_pair(n)
'''
