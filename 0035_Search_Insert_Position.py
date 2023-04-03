# Search Insert min-max or exact
class Solution:
    def searchInsert(self, nums, target):
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = (start + end)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return end+1

if __name__ == '__main__':
    nums =[1,2,3,4,5,7]
    # target = 5
    target = 6
    print(Solution().searchInsert(nums,target))
