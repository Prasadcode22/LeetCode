import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        pattern = r'[^a-zA-Z0-9]'
        new_string = re.sub(pattern, '', s)
        # print(new_string)
        reverse_string = new_string[::-1]
        # print(reverse_string)
        if new_string.lower() == reverse_string.lower():
            return True
        else:
            return False
        
if __name__ == '__main__':
    s = input()
    print(Solution().isPalindrome(s))