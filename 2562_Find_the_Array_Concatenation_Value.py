class Solution:
    def findTheArrayConcVal(self, nums):
        stack = []
        # i = -1
        b = len(nums)
        if b%2 == 1:
            x = (b//2)+1
            # stack.push(nums[x])
            y = nums[x]
            nums.remove(y)
            stack.push(y)
        i = 0
        j = len(nums)
        while i < (j/2):
            a = str(nums[i])+ str(nums[j-1])
            stack.append(int(a))
            i += 1
        return sum(stack)
    

if __name__ == '__main__':
    nums = [7,52,2,4]
    print(Solution().findTheArrayConcVal(nums))