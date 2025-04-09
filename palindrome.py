class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversed_x = 0
        temp = x
        while x > reversed_x:
            reversed_x = reversed_x * 10 + temp % 10
            temp = temp // 10
        if x == reversed_x:
            return True
        else:
            return False
