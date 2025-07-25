# source is https://leetcode.com/problems/3sum/description/

class SolutionUsingBruteForce:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        seen = set()
        n = len(nums)
        i = 0
        result = []
        target = 0
        while i < n-2:
            j = i + 1
            while j < n:
                k = j + 1
                while k < n:
                    if nums[i] + nums[j] + nums[k] == target and (nums[i], nums[j], nums[k]) not in seen:
                        result.append((nums[i], nums[j], nums[k]))
                        seen.add((nums[i], nums[j], nums[k]))
                    k += 1
                j += 1
            i += 1
        return result


class SolutionUsingHashMap:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        hashmap = defaultdict(int)
        result = []
        for num in nums:
            hashmap[num] += 1
        
        for left_idx, left_value in enumerate(nums):
            hashmap[left_value] -= 1
            if left_idx > 0 and nums[left_idx-1] == left_value:
                continue
            for mid_idx in range(left_idx+1, len(nums)-1):
                hashmap[nums[mid_idx]] -= 1
                if mid_idx > left_idx + 1 and nums[mid_idx] == nums[mid_idx-1]:
                    continue
                target = -(nums[left_idx] + nums[mid_idx])
                if hashmap[target] > 0:
                    result.append([nums[left_idx], nums[mid_idx], target])
            for idx in range(left_idx+1, mid_idx+1):
                hashmap[nums[idx]] += 1

        return result


class SolutionUsingTwoPointers:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        left_idx = -1
        result = []
        while left_idx < len(nums) - 1:
            left_idx += 1
            target = -nums[left_idx]
            middle_idx = left_idx + 1
            right_idx = len(nums) - 1
            if left_idx > 0 and nums[left_idx] == nums[left_idx - 1]:
                continue
            while middle_idx < right_idx:
                cur_sum = nums[middle_idx] + nums[right_idx]
                if cur_sum > target:
                    right_idx -= 1
                elif cur_sum < target:
                    middle_idx += 1
                else:
                    result.append([nums[left_idx], nums[middle_idx], nums[right_idx]])
                    middle_idx += 1
                    right_idx -= 1
                    while nums[middle_idx] == nums[middle_idx - 1] and middle_idx < right_idx:
                        middle_idx += 1
            
        return result




class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return SolutionUsingHashMap().threeSum(nums)
