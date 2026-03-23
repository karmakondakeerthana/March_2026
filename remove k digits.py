class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st=[]
        for ch in num:
            while st and k>0 and st[-1]>ch:
                st.pop()
                k-=1
            st.append(ch)
        if k>0:
            st=st[:-k]
        res="".join(st)
        i=0
        while i<len(res) and res[i]=='0':
            i+=1
        res=res[i:]
        return res if res else '0'
