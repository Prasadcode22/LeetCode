class Solution:
    def isValid(self, s: str) -> bool:
        # creating dict for cheching the parenthesis follows as per rules
        par = {')':'(',']':'[','}':'{'}
        # stack data structure used for pop and push operation
        stack =[]
        for c in s:
            if c in par :
                if stack and stack[-1] == par[c]:
                    # check the top of the stack element at stack[-1]
                    stack.pop() # pop the parenthesis as there is closing type 
                else:
                    return False # which means the parenthesis are in wrong order 
            else:
                stack.append(c) # push into the stack till the closing type of parenthesis doesn't occurs for its similar 
        return True if not stack else False # return true if the stack is empty or else false 

# main Function 
if __name__ =='__main__':
    s = input # User input as str
    print(Solution().isValid(s))