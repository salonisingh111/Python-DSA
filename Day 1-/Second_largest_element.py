#only for positive array
class Solution:
    def second_largest(self,nums):
        largest=nums[0]
        second_largest=-1

        for i in nums:
            if i>largest:
                second_largest=largest
                largest=i
            elif i>second_largest and i<largest:
                second_largest=i
        return second_largest
    