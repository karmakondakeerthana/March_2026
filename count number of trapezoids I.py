class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7
        from collections import defaultdict
        y_groups = defaultdict(int)
        for x, y in points:
            y_groups[y] += 1
        seg_counts = []
        for y, k in y_groups.items():
            if k >= 2:
                seg_counts.append(k * (k - 1) // 2)
        if len(seg_counts) < 2:
            return 0
        total = 0
        n = len(seg_counts)
        prefix_sum = 0
        for s in seg_counts:
            total = (total + s * prefix_sum) % MOD
            prefix_sum = (prefix_sum + s) % MOD
        return total % MOD
