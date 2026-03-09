class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        cnt=1
        endTime=intervals[0][1]
        n=len(intervals)
        for row in range(1,n):
            if(intervals[row][0]>=endTime):
                cnt+=1
                endTime=intervals[row][1]
        return n-cnt
