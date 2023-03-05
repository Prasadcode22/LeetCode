class Solution:
    def isValid(self, s: str) -> bool:
        par = {'(':')','[':']','{':'}'}
        if len(s)%2== 0:
            for i in s:
                # x = par.values[par.keys.index(i)]
                x = par.get(i)
                if x in s and s.count(i) == s.count(x):
                    return "true"
        else:
            return "false"


if __name__ =='__main__':
    s = "()[]{}"
    print(Solution().isValid(s))