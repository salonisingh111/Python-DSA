nums = [5, 8, 2, 9, 1, 9, 9,9,9]
target = 9

count=0

for i in range(len(nums)):
    if nums[i]==target:
        count+=1
print(count)
