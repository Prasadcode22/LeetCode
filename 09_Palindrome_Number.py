
def isPalindrome(num): 
    """Function to check if num is palindrome or not"""

    temp = num 
    rev = 0
    
  # Reverse the number
    while (temp > 0):
          rev = (rev * 10) + (temp % 10)
          temp //= 10

  # Check the palindrome condition
    if(num == rev): 
        return True
    else: 
        return False


# Optimal Solution using methods 
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == "".join(reversed(list(str(x))))


# class Palindrome:
#     def __init__(self, num):
#         self.number = num
        
#     # A method to check if the number is a palindrome or not
#     def is_palindrome(self):
#         s = str(self.num)
#         rev_s = ''.join(reversed(s))
#         if s == rev_s :
#             return True
#         return False  

# Driver code 
if __name__== '__main__':
    num = int(input("Enter the number :"))
    print(isPalindrome(num))
    print(isPalindrome(num))
    print(Palindrome(num))

# def is_palindrome(n):
#     s = str(n)
#     rev_s = ''.join(reversed(s))

#     return s == rev_s

# palindrome_num = int(input())



# palindrome_num = Palindrome(int(input()))





