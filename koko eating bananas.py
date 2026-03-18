from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        while(low<=high):
            mid=(low+high)//2
            sum=0
            for num in piles:
                sum+=ceil(num/mid)
            if(sum>h):
                low=mid+1
            elif(sum<=h):
                high=mid-1
        return low
