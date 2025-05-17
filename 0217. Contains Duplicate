class Solution:
    def containsDuplicateUsingSet(self, nums: List[int]) -> bool:
        unique_nums = set()
        for num in nums:
            if num in unique_nums: 
                return True
            unique_nums.add(num)
        return False


    def containsDuplicateUsingSorting(self, nums: List[int]) -> bool:
        nums.sort()
        index = 1
        while index < len(nums):
            if nums[index-1] == nums[index]:
                return True
            index += 1
        return False


    def containsDuplicateUsingHashMap(self, nums: List[int]) -> bool:
        frequencies = dict()
        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1
        return max(frequencies.values()) > 1


    def containsDuplicateUsingBruteForce(self, nums: List[int]) -> bool:
        i = 0
        while i < len(nums) - 1:
            j = i + 1
            while j < len(nums):
                if nums[i] == nums[j]:
                    return True
                j += 1
            i += 1
        return False


    def containsDuplicateUsingBitManipulation(self, nums: List[int]) -> bool:
        import struct
        min_value = 0
        max_value = struct.calcsize("P") * 8
        if min(nums) < min_value or max(nums) > max_value:
            return None
        bitmask = 0
        for num in nums:
            if (bitmask >> num) & 1:
                return True
            bitmask |= (1 << num)
        return False


    def containsDuplicate(self, nums: List[int]) -> bool:
        return self.containsDuplicateUsingSet(nums)

