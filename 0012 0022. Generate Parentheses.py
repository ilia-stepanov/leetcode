class SolutionUsingBacktracking:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def helper(open_count, close_count):
            if close_count == n:
                return result.append(''.join(curr))
            if open_count > close_count:
                curr.append(')')
                helper(open_count, close_count+1)
                curr.pop()
            if open_count < n:
                curr.append('(')
                helper(open_count+1, close_count)
                curr.pop()

        
        result = []
        curr = []
        helper(0, 0)
        return result



class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return SolutionUsingBacktracking().generateParenthesis(n)
            
