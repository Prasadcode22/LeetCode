class Solution:
    def plusOne(self, digits):
        s = ""
        for i in digits:
            s += str(i)
        
        s_1 = int(s)+1
        out = []
        for i in str(s_1):
            out.append(int(i))
        return out
if __name__ == '__main__':
    digits = [1,2,3]
    print(Solution().plusOne(digits))
    # (Solution().plusOne(digits))