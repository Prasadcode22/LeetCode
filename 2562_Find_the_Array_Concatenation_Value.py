class Solution:
    def findTheArrayConcVal(self, nums):
        stack = []
        # i = -1
        b = len(nums)
        if b%2 == 1:
            x = (b//2)
            # print(x)
            # stack.push(nums[x])
            y = nums[x]
            nums.remove(y)
            stack.append(y)
        i = 0
        j = len(nums)
        while i < (j/2):
            a = str(nums[i])+ str(nums[j-1])
            stack.append(int(a))
            i += 1
            j -= 1
        return sum(stack)
    

if __name__ == '__main__':
    nums = [7,52,13,2,4]
    print(Solution().findTheArrayConcVal(nums))