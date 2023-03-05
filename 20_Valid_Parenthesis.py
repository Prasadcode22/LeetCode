class Solution:
    def isValid(self, s: str) -> bool:
        par = {')':'(',']':'[','}':'{'}
        stack =[]
        for c in s:
            if c in par :
                if stack and stack[-1] == par[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

if __name__ =='__main__':
    s = input()
    print(Solution().isValid(s))