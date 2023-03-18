class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(i in jewels for i in stones)
    
if __name__ == '__main__':
    jewels, stones = "aA","aAAbbbb"
    print(Solution().numJewelsInStones(jewels,stones))