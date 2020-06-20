def quad(nums):
    list_of_dup = []
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            duplicate_num = nums[i]
            list_of_dup.append(duplicate_num)
    for num in list_of_dup:
        count = nums.count(num)
        if count == 4:
            return 8
    if TypeError:
        return 0



# Testing
'''
n = [2, 4, 4, 4, 11, 14, 4]
quad(n)
'''