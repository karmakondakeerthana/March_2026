from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        d=Counter(s)
        u_d=sorted(d.items(),key=lambda x:-x[1])
        result=""
        for key,value in u_d:
            result+=key*value
        return result
