from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d=Counter(nums)
        u_d=sorted(d.items(),key=lambda x:(x[1],-x[0]))
        result=[]
        for key,value in u_d:
            for i in range(value):
                result.append(key)
        return result
