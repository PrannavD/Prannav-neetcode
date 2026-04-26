class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        result   = nums[0]
        max_prod = nums[0]
        min_prod = nums[0]
        
        for num in nums[1:]:
            temp     = max_prod                              # save before overwrite
            max_prod = max(num, num * temp, num * min_prod) # best of 3 candidates
            min_prod = min(num, num * temp, num * min_prod) # worst of 3 candidates
            result   = max(result, max_prod)                 # update global best
        
        return result
        