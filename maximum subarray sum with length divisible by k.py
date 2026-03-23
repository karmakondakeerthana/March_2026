class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = 0
        mod_min = {i: float('inf') for i in range(k)}
        mod_min[0] = 0 
        ans = float('-inf')
        for i, num in enumerate(nums):
            prefix += num
            mod_class = (i + 1) % k  
            if mod_min[mod_class] != float('inf'):
                ans = max(ans, prefix - mod_min[mod_class])
            mod_min[mod_class] = min(mod_min[mod_class], prefix)
        return ans
