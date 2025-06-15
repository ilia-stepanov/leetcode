class Solution:

    def encode(self, strs: List[str]) -> str:
        sep = '|'
        for index, string in enumerate(strs):
            length = len(string)
            strs[index] = f'{length}{sep}{string}'
        return ''.join(strs)

    def decode(self, s: str) -> List[str]:
        left = 0
        right = 0
        result = []
        while right < len(s):
            if s[right] == '|':
                value_length = int(s[left:right])
                value = s[right+1:right+1+value_length]
                result.append(value)
                left = right+1+value_length
                right = left
            right += 1
        return result
