class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        new = s.split()
        for x, item in enumerate(new):
            new[x] = item[::-1]
        return ' '.join(new)