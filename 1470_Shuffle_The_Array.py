
from ast import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a, b = nums[:n], nums[n:]
        res = []
        for i in range(n):
            res.append(a[i])
            res.append(b[i])
        return res