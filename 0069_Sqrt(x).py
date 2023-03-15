import math
class Solution:
    def mySqrt(self, x: int) -> int:
        return int(math.sqrt(x))
    

if __name__ == '__main__':
    x = 9.388
    print(Solution().mySqrt(x))