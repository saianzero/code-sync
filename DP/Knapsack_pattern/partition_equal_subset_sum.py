"""
https://leetcode.com/problems/partition-equal-subset-sum/description/

We can split an even sum equally.
For example: sum = 22
if one subset sums to 11, the remaining elements (forming another subset) automatically sum to 11, total 22.
"""

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_ = 0
        for num in nums:
            sum_+=num
        if sum_%2 != 0:
            return False
        elif sum_%2 == 0:

            # Give me the subset that has a sum equal to sum_//2
            # because if we find a single subset whose sum is sum_//2, 
            # the remaining elements will obv sum up to sum_//2 
            # since the total subset sum is sum_
            return self.isSubsetSum(nums, sum_//2)
    
    def isSubsetSum(self, arr: list[int], sum: int) -> bool:
        n = len(arr)
        
        t = [[False]*(sum+1) for _ in range(n+1)]
        
        for i in range(n+1):
                t[i][0] = True
        
        for i in range(1, n+1):
            for j in range(1, sum+1):
        
                
                if arr[i-1] <= j:
                    t[i][j] = (t[i-1][j-arr[i-1]]) or (t[i-1][j])
                    
                else:
                    t[i][j] = t[i-1][j]
            
        return t[n][sum]
    