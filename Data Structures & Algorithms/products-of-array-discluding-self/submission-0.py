class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        output = [1] * n

        # Prefix product
        for i in range(1, n):
            output[i] = output[i - 1] * nums[i - 1]

        right_multiplier = 1

        # Suffix product
        for i in range(n - 1, -1, -1):

            output[i] *= right_multiplier

            right_multiplier *= nums[i]

        return output