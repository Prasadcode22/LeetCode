from ast import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            a = nums[i]
            res.append(nums[a])
        return res

            
        