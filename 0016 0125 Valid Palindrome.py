class SolutionUsingReverseString:
    def isPalindrome(self, s: str) -> bool:
        corrected_s = []
        for char in s:
            if char.isalnum():
                corrected_s.append(char.lower())
        
        return corrected_s == corrected_s[::-1]


class SolutionUsingSlidingWindow:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        s = s.lower()
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
        return True


class Solution:
    def isPalindrome(self, s: str) -> bool:
        return SolutionUsingReverseString().isPalindrome(s)
