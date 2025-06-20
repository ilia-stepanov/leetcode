class SolutionUsingStack:
    def isValid(self, s: str) -> bool:
        stack = []
        open_chars = {'(', '[', '{'}
        pairs = {'}':'{', ')':'(', ']':'['}
        for char in s:
            if char in open_chars:
                stack.append(char)
            elif not stack or pairs[char] != stack.pop():
                return False
        if stack:
            return False
        return True

        
class Solution:
    def isValid(self, s: str) -> bool:
        return SolutionUsingStack().isValid(s)

        
