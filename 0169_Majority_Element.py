from ast import List


class Solution:
    def majorityElement(self, nums):
        out= []
        max_count, max_count_element = 0, 0
        for i in nums:
            if i not in out:
                if nums.count(i) > max_count:
                    max_count = nums.count(i)
                    max_count_element = i
        return max_count_element   
    
if __name__ == '__main__':
    nums = [1,2,3,2,1,2,3,1,2]
    print(Solution().majorityElement(nums))
    