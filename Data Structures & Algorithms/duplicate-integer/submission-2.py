class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num=set(nums)
        if len(nums)!=len(num):
            return True
        else:
            return False

        # n=len(nums)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i]==nums[j]:
        #             return True
                
        # return False
        