class Solution:
    def removeDuplicates(self, nums):
        res = []
        for i in nums:
            if i not in res:
                res.append(i)
            else:
                res[-1] = '_'
                x = res[-1]
                res.append(x)
            
        return res


#   
    def removeDuplicates_(self, nums):
        l = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[l] = nums[i]
                l += 1
        return nums
    
    
if __name__ == '__main__':
    nums = [1,1,2]
    # nums = input()
    print(Solution().removeDuplicates_(nums))
