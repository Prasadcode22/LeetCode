class Solution:
    def climbStairs(self, n: int) -> int:
        if n <=3:
            return n
        arr = [0,1,2,3]

        for i in range(4, n+1):
            arr.append(arr[i-1]+arr[i-2])

        return arr.pop()