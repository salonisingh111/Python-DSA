nums = [5, 8, 2, 9, 1]

count=nums[0]
for i in nums:
    if i>count:
        count=i
print(count)
