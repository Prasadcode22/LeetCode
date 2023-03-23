class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(x[1:] for x in sorted(i[-1]+i[:-1] for i in s.split()))