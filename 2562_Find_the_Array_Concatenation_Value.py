class Solution:
    def findTheArrayConcVal(self, nums):
        sum = 0
        # i = -1
        b = len(nums)
        # print(b)
        if b%2 == 1:
            x = b//2
            # print(x)
            # stack.push(nums[x])
            y = nums[x]
            sum += y
            # print(y)
            del nums[x]
            
        # print(sum)
        # print(nums)
        i = 1
        j = len(nums)
        z= (j/2)+1
        # print(j)
        while i < z:
            a = str(nums[i-1])+ str(nums[j-1])
            sum +=(int(a))
            # print(sum)
            i += 1
            j -= 1
        return sum
if __name__ == '__main__':
    nums = [40,78,21,41,40,75,3,10,91,10,3,48,3,96,100,5,97,36,93,81,29]
    # nums = [1,78,27,48,14,86,79,68,77,20,57,21,18,67,5,51,70,85,47,56,22,79,41,8,39,81,59,74,14,45,49,15,10,28]
    print(Solution().findTheArrayConcVal(nums))