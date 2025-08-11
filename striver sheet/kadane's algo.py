from typing import List
import sys

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = -sys.maxsize-1
        summ = 0
        # if n>1:
            # sub_sum = []
        for i in range(n):
            summ += nums[i]
            if summ > maxi:
                maxi = summ
            if summ < 0:
                summ =0 
            #     for j in range(i, n+1):
            #         if sum(nums[i:j])!=0 and 0 not in nums:
            #             sub_sum.append(sum(nums[i:j]))
            #         if 0 in nums:
            #             sub_sum.append(sum(nums[i:j]))
            # print(sub_sum)
        return maxi
        # if n==1:
        #     return nums[0]

sol = Solution()
nums = [5,4,-1,7,8]#[-1,0]#[-2,-1]#]#[-2, 1, -3, 4, -1, 2, 1, -5, 4]#[1]
print(sol.maxSubArray(nums=nums))
