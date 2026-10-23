class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st=set(nums)
        n=len(nums)
        max_count=0

        for n in st:
            if n-1 not in st:
                length=0
                while n+length in st:
                    length+=1
                max_count=max(max_count,length)
        return max_count
        