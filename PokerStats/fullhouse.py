def full_house(nums):
    def remove_values(lst, val):
        return [value for value in lst if value != val]
    list_of_dup = []
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            duplicate_num = nums[i]
            list_of_dup.append(duplicate_num)
    for num in list_of_dup:
        count = nums.count(num)
        if count == 3:
            new_lst = remove_values(list_of_dup, num)
            for num2 in new_lst:
                count2 = nums.count(num2)
                if count2 >= 2:
                    return 7
    if TypeError:
        return 0

# Testing
'''
n = [1, 3, 9, 9, 9, 14, 14]
print(full_house(n))
'''