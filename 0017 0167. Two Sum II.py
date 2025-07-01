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
        

class SolutionUsingBinarySearch:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def bs(left, right, arr, target):
            if left >= right:
                return -1
            mid = left + (right - left) // 2
            print(left, right, mid)
            if arr[mid] > target:
                return bs(left, mid - 1, arr, target)
            elif arr[mid] < target:
                return bs(mid + 1, right, arr, target)
            else:
                return mid


        for left_idx, left_value in enumerate(numbers):
            right_value = target - left_value
            right_idx = bs(left_idx+1, len(numbers)-1, numbers, target)
            if right_idx != -1:
                return [left_idx+1, right_idx+1]
        return [1, 2]


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        return SolutionUsingBinarySearch().twoSum(numbers, target)
        
