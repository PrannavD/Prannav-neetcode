class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i , num in enumerate(nums):
            y = target - nums[i]

            if y in seen:
                return[seen[y],i]
        
            seen[num] = i


