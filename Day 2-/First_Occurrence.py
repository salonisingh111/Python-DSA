nums = [5, 8, 9, 2, 9, 1]
target = 9

result=False

for i in range (len(nums)):
    if nums[i]==target:
        result=True
        print(i)
        break
if result==False:
    print("Not Found")