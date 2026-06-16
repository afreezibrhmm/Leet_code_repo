def move_zeros(nums):
    write_index = len(nums)-1
    for read_index in range(len(nums)):
        if nums[read_index] !=0:
            nums[write_index],nums[read_index] = nums[read_index],nums[write_index]
            write_index-= 1
    return nums

arr1 = [0,1,2,0,5,0,6,4,3,0,0,5,0,5]
arr2 = [0,2,5,8,4,1,0,0,4,0,5]

print(f"Original:{arr1},modified:{move_zeros(arr1)}")
print(f"Original:{arr2},modified:{move_zeros(arr2)}")