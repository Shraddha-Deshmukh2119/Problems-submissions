class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""

        need={}
        window={}
        for c in t:
            need[c]=need.get(c,0)+1

        left=0
        have=0
        required=len(need)
        min_len=float('inf')
        result=""

        for r in range(len(s)):
            c=s[r]
            window[c]=window.get(c,0)+1

            if c in need and window[c]==need[c]:
                have+=1

            while have==required:

                if r-left+1<min_len:
                    min_len=r-left+1
                    result=s[left:r+1]

                ch=s[left]
                window[ch]-=1

                if ch in need and window[ch]<need[ch]:
                    have-=1

                left+=1
        return result
        