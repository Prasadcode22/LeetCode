class Solution:
    def singleNumber(self, nums):
        out = 0
        for i in range(len(nums)):
            a = nums[i]
            if nums.count(a) == 1 :
                out = a
        return out

if __name__ == '__main__':
    nums = [4,1,2,1,2]
    print(Solution().singleNumber(nums))