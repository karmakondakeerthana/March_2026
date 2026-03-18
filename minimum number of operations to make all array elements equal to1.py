from math import gcd
from functools import reduce
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        overall_gcd = nums[0]
        for x in nums:
            overall_gcd = gcd(overall_gcd, x)
        if overall_gcd != 1:
            return -1
        ones = nums.count(1)
        if ones > 0:
            return n - ones
        min_len = float('inf')
        for i in range(n):
            g = nums[i]
            for j in range(i + 1, n):
                g = gcd(g, nums[j])
                if g == 1:
                    min_len = min(min_len, j - i + 1)
                    break
        return (min_len - 1) + (n - 1)
