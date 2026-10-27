class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1

        while l<r:
           

            mid=(l+r)//2
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid
        return nums[l]
        # l=0
        # r=len(nums)-1
        # ans=nums[0]

        # while l<=r:
        #     if nums[l]<=nums[r]:
        #         ans=min(ans,nums[l])
        #         break
        #     mid=(l+r)//2
        #     ans=min(ans,nums[mid])

        #     if nums[mid]>=nums[l]:
        #         l=mid+1
        #     else:
        #         r=mid-1
        # return ans
        