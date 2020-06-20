def trip(nums):
    list_of_dup = []
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            duplicate_num = nums[i]
            list_of_dup.append(duplicate_num)
    for num in list_of_dup:
        count = nums.count(num)
        if count == 3:
            return 4
    if TypeError:
        return 0


# Testing
'''
n = [2, 4, 3, 3, 11, 14, 2, 1]
trip(n)
'''
