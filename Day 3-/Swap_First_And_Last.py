nums = [10, 20, 30, 40]

left=0
right=len(nums)-1

nums[left], nums[right]=nums[right],nums[left]
print(nums)