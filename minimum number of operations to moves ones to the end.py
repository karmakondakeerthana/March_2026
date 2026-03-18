class Solution:
    def maxOperations(self, s: str) -> int:
        ones = 0
        ops = 0
        n = len(s)
        for i, ch in enumerate(s):
            if ch == '1':
                ones += 1
            else:  # ch == '0'
                if i > 0 and s[i-1] == '1':
                    ops += ones
        return ops
