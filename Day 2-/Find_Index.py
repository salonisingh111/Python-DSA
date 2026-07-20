nums = [5, 8, 2,  1]

target = 9


def find_index(nums):
    result=False
    for i in range (len(nums)):
        if nums[i] == target:
            result=True
            print(i)
            
    if result==False:
        print("Not Found")

find_index(nums)