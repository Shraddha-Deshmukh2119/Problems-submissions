import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}

        for num in nums:
            if num not in freq:
                freq[num]=1
            else:
                freq[num]+=1
        
        heap=[]
        for num in freq:
            heapq.heappush(heap,(freq[num],num))

            if len(heap)>k:
                heapq.heappop(heap)
        
        ans=[]
        for freq,num in heap:
            ans.append(num)
        
        return ans

        
        