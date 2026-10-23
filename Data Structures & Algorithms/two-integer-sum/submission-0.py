class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        Hashmap={}
        for i in range(n):
            diff=target-nums[i]
            if diff in Hashmap:
                return [Hashmap[diff],i]
            Hashmap[nums[i]]=i
        