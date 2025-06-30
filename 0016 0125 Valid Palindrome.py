class SolutionUsingBruteForce:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i = 0
        while i < n:
            j = i + 1
            while j < n:
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
                j += 1
            i += 1
        return [1, 2]


class SolutionUsingHashmap:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = dict()
        for idx, num in enumerate(numbers):
            if num in hashmap:
                hashmap[num].append(idx)
            else:
                hashmap[num] = [idx]
        for num1, idx1 in hashmap.items():
            num2 = target - num1
            if num2 not in hashmap:
                continue

            if num1 == num2:
                idx2 = hashmap[num2][1]
            else:
                idx2 = hashmap[num2][0]

            idx1 = idx1[0]
            if idx2 > idx1:
                return [idx1+1, idx2+1]
            return [idx2+1, idx1+1]
        return [1, 2]
                
        
class SolutionUsingTwoPointes:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum > target:
                right -= 1
            elif curr_sum < target:
                left += 1
            else:
                return [left+1, right+1]
        return [1, 2]
        

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        return SolutionUsingTwoPointes().twoSum(numbers, target)
        
