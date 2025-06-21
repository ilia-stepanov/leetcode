class Solution:
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
