# 1365. How Many Numbers Are Smaller Than the Current Number
class Solution:
    def smallerNumbersThanCurrent(self, nums):
        res = []
        s = sorted(nums)
        for i in nums:
            a = s.index(i)
            res.append(len(s[:a]))
        return res

if __name__ == '__main__':
    nums = [8,1,2,2,3]
    
    print(Solution().smallerNumbersThanCurrent(nums))