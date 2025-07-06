class SolutionUsingTwoPointers:
    def maxArea(self, height: List[int]) -> int:
        left_idx = 0
        right_idx = len(height) - 1
        max_volume = 0

        while left_idx < right_idx:
            left_val = height[left_idx]
            right_val = height[right_idx]

            max_volume = max(min(left_val, right_val) * (right_idx - left_idx), max_volume)
            
            if right_val >= left_val:
                left_idx += 1
            else:
                right_idx -= 1
        
        return max_volume
