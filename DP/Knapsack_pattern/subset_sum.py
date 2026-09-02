# https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1

# Recursion - TLE 
class Solution:
    def isSubsetSum(self, arr: list[int], sum: int) -> bool:
        # code here
        n = len(arr)
        
        def solve(sum, n):
            
            if sum == 0:
                return True
            
            if n == 0:
                return False
            
            if arr[n-1] <= sum:
                # include
                inc = solve(sum-arr[n-1], n-1)
                #exclude
                exc = solve(sum, n-1)
                
                return inc or exc
            else:
                exc = solve(sum, n-1)
                return exc
        
        return solve(sum, n)

# Memoization
class Solution:
    def isSubsetSum(self, arr: list[int], sum: int) -> bool:
        # code here
        n = len(arr)
        t = [[-1]*(sum+1) for _ in range(n+1)]
        
        def solve(sum, n):
            if sum == 0:
                return True
            
            if n == 0:
                return False
            
            if t[n][sum] != -1:
                return t[n][sum]
            
            if arr[n-1] <= sum:
                inc = solve(sum-arr[n-1], n-1)
                exc = solve(sum, n-1)
                t[n][sum] = inc or exc
            else:
                t[n][sum] = solve(sum, n-1)
            
            return t[n][sum]
                
            
        return solve(sum, n)

# Tabulation
class Solution:
    def isSubsetSum(self, arr: list[int], sum: int) -> bool:
        # code here
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
            