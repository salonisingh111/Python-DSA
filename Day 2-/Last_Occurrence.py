nums = [5, 8, 9, 2, 9, 1, 9]
target = 9

result=False
last_index=-1

for i in range (len(nums)):
    if nums[i]==target:
        result=True
        last_index=i


if result==True:
    print(last_index)
else:
    print("Not Found")

       
    
