# source is https://leetcode.com/problems/car-fleet/

from math import ceil

class Solution:
  # not finished
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ls = [(pos, speed[idx], ceil((target - pos) / speed[idx])) for idx, pos in enumerate(position)]
        ls.sort()
        stack = []
        result = len(speed)

        for idx, next_data in enumerate(ls):
            next_pos, next_speed, next_time = next_data
            while stack and stack[-1][2] <= next_time:
                result -= 1
                stack.pop()
            stack.append(next_time)
        return result

