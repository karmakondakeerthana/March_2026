class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)   
        Z = [0] * (n+1)
        O = [0] * (n+1)       
        for i, ch in enumerate(s):
            Z[i+1] = Z[i] + (ch == '0')
            O[i+1] = O[i] + (ch == '1')  
        max_zeros = Z[-1]
        groups = [[] for _ in range(max_zeros+1)]
        for i in range(n+1):
            groups[Z[i]].append(i)
        ans = 0
        import bisect
        MAXK = int(n**0.5) + 3
        for k in range(MAXK):
            if k > max_zeros:
                break
            k_sq = k*k
            for z in range(max_zeros - k + 1):
                group_l = groups[z]         
                group_r = groups[z + k]
                O_l = [O[idx] for idx in group_l]
                for r_idx in group_r:
                    val = O[r_idx] - k_sq
                    pos = bisect.bisect_left(group_l, r_idx)
                    count = bisect.bisect_right(O_l, val, 0, pos)
                    ans += count
        return ans
