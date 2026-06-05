class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for i , val in enumerate(nums):
            compliment=target-val
            if compliment in hash:
                return [hash[compliment],i]
            hash[val]=i