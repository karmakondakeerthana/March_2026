from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d=Counter(nums)
        n=len(nums)
        result=[]
        for key,value in d.items():
            if(value>n//3):
                result.append(key)
        return result
