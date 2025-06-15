class Solution:

    def productExceptSelfUsingDivision(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total_mult = 1
        zero_count = 0

        for v in nums:
            if v != 0:
                total_mult *= v
            else:
                zero_count += 1

        if zero_count > 1:
            return [0] * n
        
        if zero_count == 1:
            for i, v in enumerate(nums):
                if v == 0:
                    nums[i] = total_mult
                else:
                    nums[i] = 0
            return nums

        for i, v in enumerate(nums):
            nums[i] = total_mult // nums[i]
        return nums


    def productExceptSelfUsingPrefixSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cum_arr = [1] * n
        mult = 1
        for i, v in enumerate(nums):
            cum_arr[i] *= mult
            mult *= v

        mult = 1
        for i in range(n-1, -1, -1):
            cum_arr[i] *= mult
            mult *= nums[i]
        
        return cum_arr

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return self.productExceptSelfUsingDivision(nums)
