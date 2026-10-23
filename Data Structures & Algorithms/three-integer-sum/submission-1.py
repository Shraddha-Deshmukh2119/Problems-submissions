class Solution:
    def threeSum(self, arr: list[int]) -> list[list[int]]:
        n = len(arr)
        ans = []
        arr.sort()

        for i in range(n):
            if i!=0 and arr[i]==arr[i-1]:
                continue
            l=i+1
            r=n-1
            while l<r:
                total_sum=arr[i]+arr[l]+arr[r]
                if total_sum>0:
                    r-=1
                elif total_sum<0:
                    l+=1
                else:
                    temp=[arr[i],arr[l],arr[r]]
                    ans.append(temp)
                    l+=1
                    r-=1

                    while l<r and arr[l]==arr[l-1]:
                        l+=1
                    while l<r and arr[r]==arr[r+1]:
                        r-=1
        return ans




       
