class SolutionUsingOneStack:
    def evalRPN(self, tokens: List[str]) -> int:
        def compute(left_value, right_value, token):
            if token == '+':
                return left_value + right_value
            if token == '-':
                return left_value - right_value
            if token == '*':
                return left_value * right_value
            if token == '/':
                return int(left_value / right_value)

        operators = {'+', '-', '*', '/'}
        stack = []
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                right_value = stack.pop()
                left_value = stack.pop()
                result = compute(left_value, right_value, token)
                stack.append(result)
        return stack[0]


class SolutionUsingRecursion:
    def compute(self, left_value, right_value, token):
        if token == '+':
            return left_value + right_value
        if token == '-':
            return left_value - right_value
        if token == '*':
            return left_value * right_value
        if token == '/':
            return int(left_value / right_value)

    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        def dfs():
            token = tokens.pop()

            if token not in operators:
                return int(token)
            
            right_value = dfs()
            left_value = dfs()

            return self.compute(left_value, right_value, token)

        return dfs()


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        return SolutionUsingRecursion().evalRPN(tokens)
