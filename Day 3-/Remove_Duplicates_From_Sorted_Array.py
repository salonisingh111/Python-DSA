nums = [1, 1, 2, 2, 3, 4, 4, 5]

output=[]

for i in range(len(nums)):
    if nums[i] in output:
        i+=1
    else:
        output.append(nums[i])
print(output)