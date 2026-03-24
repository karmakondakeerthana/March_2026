class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ma=0
        st=[]
        for i in range (len(heights)):
            h=heights[i]
            start=i
            while st and st[-1][1]>h:
                idx,height=st.pop()
                ma=max(ma,height*(i-idx))
                start=idx
            st.append((start,h))
        for idx,height in st:
            ma=max(ma,height*(len(heights)-idx))
        return ma
