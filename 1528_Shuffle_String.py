# Restore the String
class Solution:
    def restoreString(self, s, indices):
        out = ['']*len(s)
        for index, char in enumerate(s):
            out[indices[index]]= char
        return ''.join(out)
    
if __name__ == '__main__':
    s = "codeleet"
    indices = [4,5,6,7,0,2,1,3]
    print(Solution().restoreString(s, indices))
