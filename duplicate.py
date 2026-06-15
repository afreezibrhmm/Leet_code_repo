def duplicate(nums):
    unique_nums = set(nums)

    if len (unique_nums)!=len(nums):
        return True
    else:
        return False
    
list1 = [1,2,3,1]
list2 = [1,2,3,4]

print(f"does {list1} have duplicates?",duplicate(list1))
print(f"does {list2} have duplicates?",duplicate(list2))
