nums=['h','e','l','l','o']

class Solution:
    def reverse_array(self,nums):
        left=0
        right=len(nums)-1
        
        while left <right:
            nums[left], nums[right]=nums[right],nums[left]

            left +=1
            right -=1
        return nums
obj=Solution()
obj.reverse_array(nums)
print(obj.reverse_array(nums))
