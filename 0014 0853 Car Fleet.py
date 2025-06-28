# source is https://leetcode.com/problems/car-fleet/

class SolutionUsingStack:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ls = [(pos, speed[idx], (target - pos) / speed[idx]) for idx, pos in enumerate(position)]
        ls.sort()
        stack = []
        result = len(speed)

        for idx, next_data in enumerate(ls):
            next_pos, next_speed, next_time = next_data
            while stack and stack[-1][2] <= next_time:
                result -= 1
                stack.pop()
            stack.append(next_data)
        return result


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        return SolutionUsingStack().carFleet(target, position, speed)
