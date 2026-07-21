nums = [10, 20, 30, 40, 50]

for i in range(len(nums)-1):
    nums[i] = nums[i+1]
print(nums)