"""
0/1 KNAPSACK
 
Given a knapsack of total weight W,
Input arrays - Wt and Val, correspond to wt and val of ith item
The choice is to add that item to knapsack or not to add. (No partial for 0-1 case),
to get the MAXIMUM Profit/Weight added to the knapsack.

Why DP:
1. Choice
2. Optimal (find max)

Approach:
1. Recursion
2. Memoization
3. Tabulation
"""

class Sol:
    # 1. Recursive Approach, right to left on the input arrays.
    def knapsack(self, wt, val, W, n):
        # Arrive at the base condition by taking the smallest possible inputs and finding the output for that
        if n == 0 or W == 0:
            return 0

        if wt[n-1] <= W:
            # choice 1 - Add to knapsack (curr cell + remaining)
            added = val[n-1] + self.knapsack(wt, val, W-wt[n-1], n-1)
             # choice 2 - Do not add to knapsack (only remaining)
            not_added = self.knapsack(wt,val,W, n-1)
            return max(added, not_added)
        else: # No choice, cannot add if weight of item is more than the weight of the knapsack
            return self.knapsack(wt,val,W, n-1)

    # 2. Memoization Approach
    # How many variables are changing in the recursive fn -> 2 variables -  n, W
    # 2D array memoization - t[n][W], initialize with -1 initially
  
    def knapsack(self, wt, val, W, n):
        t = [[-1] * (W + 1) for _ in range(n + 1)]

        def solve(W, n):
            if n == 0 or W == 0:
                return 0

            if t[n][W] != -1:
                return t[n][W]

            if wt[n - 1] <= W:
                added = val[n - 1] + solve(W - wt[n - 1], n - 1)
                not_added = solve(W, n - 1)

                t[n][W] = max (added, not_added)
            else:
                t[n][W] = solve(W, n - 1)

            return t[n][W]

        return solve(W, n)

    # 3. Tabulation Approach
    def knapsack(self, wt, val, W, n):
        # Base case handled like this
        # t[i][j] = maximum value using first i items having knapsack capacity j
        # t[0][j] = 0  -> no items
        # t[i][0] = 0  -> knapsack capacity is 0
        t = [[0] * (W + 1) for _ in range(n + 1)]


        for i in range(1, n + 1):
            for j in range(1, W + 1):

                if wt[i - 1] <= j:
                    # Choice 1: include current item
                    added = val[i - 1] + t[i - 1][j - wt[i - 1]]

                    # Choice 2: don't include current item
                    not_added = t[i - 1][j]

                    t[i][j] = max(added, not_added)

                else:
                    # Current item cannot fit
                    t[i][j] = t[i - 1][j]

        return t[n][W]