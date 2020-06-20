def pair(nums):
    list_of_dup = []
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            duplicate_num = nums[i]
            list_of_dup.append(duplicate_num)
    no_dup = list(dict.fromkeys(list_of_dup))
    if len(no_dup) >= 1:
        return 2
    else:
        return 0


# Testing
'''
n = [1, 2, 3, 5, 5, 14]
print(pair(n))
'''
