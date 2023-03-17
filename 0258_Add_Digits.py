class Solution:
    def addDigits(self, num: int) -> int:
        a = str(num)
        if num > 9:
            sum = 0
            for i in a:
                sum += int(i)
            return  Solution().addDigits(sum)
        else:
            return num
    
    def addDigits(self, num: int) -> int:
        return 1 + (num-1)
if __name__ == '__main__':
    num = 0
    print(Solution().addDigits(num))          
