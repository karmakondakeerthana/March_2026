class Solution(object):
    def majorityElement(self, nums):
       n=len(nums)
       d={}
       for i in nums:
        if(i in d):
            d[i]=d[i]+1
        else:
            d[i]=1
       for key,value in d.items():
        if(value>n//2):
            return key
