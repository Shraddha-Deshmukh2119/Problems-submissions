class Solution:
    def isalphanumeric(self,ch):
        x=ord(ch)
        if (ord('A')<=x<=ord('Z') or ord('a')<=x<=ord('z') or ord('0')<=x<=ord('9')):
            return True
        return False
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()

        l=0
        r=len(s)-1
        while l<r:
            if l<r and not self.isalphanumeric(s[l]):
                l+=1
            elif r>l and not self.isalphanumeric(s[r]):
                r-=1
            elif s[l]==s[r]:
                l+=1
                r-=1
            else:
                return False
        return True

        