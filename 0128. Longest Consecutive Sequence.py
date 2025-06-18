class SolutionUsingSorting:
    # O(NlogN)
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = list(set(nums))
        nums.sort()
        max_counter = 1
        n = len(nums) - 1
        cur_counter = 1
        for i, v in enumerate(nums):
            if i == n:
                break
            if v + 1 == nums[i+1]:
                cur_counter += 1
                max_counter = max(max_counter, cur_counter)
            else:
                cur_counter = 1
        return max_counter

class SolutionUsingBucketSorting:
    # O(N) but Memory Limit Exceeded
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_value = max(nums)
        min_value = min(nums)
        buckets = (max_value - min_value + 1) * [0]
        for num in nums:
            buckets[num - min_value] = 1
        
        max_counter = 1
        cur_counter = 0
        for bucket in buckets:
            if bucket == 0:
                max_counter = max(max_counter, cur_counter)
                cur_counter = 0
            else:
                cur_counter += 1
        max_counter = max(max_counter, cur_counter)
        return max_counter      


class SolutionUsingHashMapGraph:
    # Time Limit Exceeded
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        hashmap = dict()
        for num in nums:
            hashmap[num] = num + 1
        max_counter = 1
        for key, value in hashmap.items():
            cur_counter = 1
            while value in hashmap:
                cur_counter += 1
                value = hashmap[value]
            max_counter = max(max_counter, cur_counter)
        max_counter = max(max_counter, cur_counter)
        return max_counter      


class SolutionUsingSet1:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = set(nums)
        seen = set()
        max_counter = 1
        
        for num in nums:
            cur_counter = 1
            if num in seen:
                continue
            num_up = num + 1
            num_down = num - 1
            while num_up in nums and num_up not in seen:
                seen.add(num_up)
                num_up += 1
            cur_counter += num_up - num - 1
            while num_down in nums and num_down not in seen:
                seen.add(num_down)
                num_down -= 1
            cur_counter += num - num_down - 1
            max_counter = max(max_counter, cur_counter)
        return max_counter      


class SolutionUsingSet2:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        max_counter = 1
        for num in nums:
            cur_counter = 1
            if num - 1 in nums:
                continue
            num_up = num + 1
            while num_up in nums:
                num_up += 1
            cur_counter += num_up - num - 1
            max_counter = max(max_counter, cur_counter)
        return max_counter    


class SolutionUsingHashMap:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hashmap = defaultdict(int)
        max_counter = 1
        for num in nums:
            if hashmap[num]:
                continue
            hashmap[num] = hashmap[num - 1] + hashmap[num + 1] + 1
            hashmap[num - hashmap[num - 1]] = hashmap[num]
            hashmap[num + hashmap[num + 1]] = hashmap[num]
            max_counter = max(max_counter, hashmap[num])
        return max_counter

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        return SolutionUsingHashMap().longestConsecutive(nums)
