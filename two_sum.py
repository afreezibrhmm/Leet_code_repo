def two_sum(nums,target):
    seen_nmbrs = {}

    for index,curr_num in enumerate(nums):
        needed_num = target-curr_num

        if needed_num in seen_nmbrs:
            return[seen_nmbrs[needed_num],index]
        
        seen_nmbrs[curr_num] = index

numbers = [2,7,11,15]
target_value = 9
result = two_sum(numbers,target_value)
print(f"The indices of numbers that add up to {target_value} are : {result}")