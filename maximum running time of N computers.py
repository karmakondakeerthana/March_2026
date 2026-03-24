class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        total = sum(batteries)
        left, right = 0, total // n
        def canRun(t):
            usable = 0
            for b in batteries:
                usable += min(b, t)
            return usable >= t * n
        while left < right:
            mid = (left + right + 1) // 2
            if canRun(mid):
                left = mid
            else:
                right = mid - 1      
        return left
