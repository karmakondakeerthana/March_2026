class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        d = {}
        left = 0
        right=0
        max_len = 0
        while(right<n):
            if s[right] in d and d[s[right]] >= left:
                left = d[s[right]] + 1
            d[s[right]]=right
            max_len = max(max_len, right - left + 1)
            right+=1
        return max_len
