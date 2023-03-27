class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        res = []
        # min_cand = min(candies)
        max_cand = max(candies)
        for i in range(len(candies)):
            add_extracandies = candies[i] + extraCandies
            if add_extracandies > max_cand:
                res.append(True)
            else :
                res.append(False)
        return res


if __name__ == '__main__':
    candies = [4,2,1,1,2]
    extraCandies = 1
    print(Solution().kidsWithCandies(candies, extraCandies))