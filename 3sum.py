class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n=len(nums)
        s=set()
        for i in range(0,n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if(nums[i]+nums[j]+nums[k]==0):
                        lst=[nums[i],nums[j],nums[k]]
                        lst.sort()
                        s.add(tuple(lst))
        ans=[]
        for t in s:
            ans.append(list(t))
        return ans
