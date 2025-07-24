class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start_index = 0
        curr_char_sequence = s[0]
        next_start = None
        max_length = 0
        curr_idx = 1
        curr_k = k
        while curr_idx < len(s):
            if s[curr_idx] != curr_char_sequence:
                if not next_start:
                    next_start = curr_idx
                if curr_k == 0:
                    max_length = max(max_length, curr_idx - start_index)
                    curr_idx = next_start
                    curr_k = k + 1
                    start_index = next_start
                    next_start = None
                    curr_char_sequence = s[start_index]
                curr_k -= 1
            curr_idx += 1
            max_length = max(max_length, curr_idx - max(0, start_index - min(curr_k, max(0, len(s) - start_index))))

        start_index = max(0, start_index - min(curr_k, max(0, len(s) - start_index)))
        max_length = max(max_length, curr_idx - start_index)
        return max_length


