class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        if not strs:
            return res
        for i in range(len(strs[0])):
            char = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != char:
                    return res
            res += char 
        return res
    
if __name__ == '__main__':
    strs = ["flower","flow","flight"]
    print(Solution().longestCommonPrefix(strs))