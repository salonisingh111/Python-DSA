nums = [10, 20, 30, 40, 50]

left=0

right=len(nums)-1

for i in range(len(nums)):
    if left<right:
        nums[left], nums[right]=nums[right],nums[left]
        left +=1
        right-=1
print(nums)