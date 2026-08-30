"""
https://leetcode.com/problems/valid-arrangement-of-pairs/

Hierholzer's Algorithm

1. Build adj list
2. Build indegree and outdegree for each node
3. identify the start node (outdegree-indegree == 1)
4. FIll the stack if edges exist
5. Pop the stack if no more edges remaining, store it in path, reverse the path to get the correct order
"""

from typing import List
from collections import defaultdict
class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        indegree = defaultdict(int)
        outdegree = defaultdict(int)

        for u, v in pairs:
            adj[u].append(v)
            outdegree[u]+=1
            indegree[v]+=1
        

        start = pairs[0][0]
        for u in adj:
            if outdegree[u]-indegree[u] == 1:
                start = u

       
        stack = [start]
        path = []
        while stack:
            u = stack[-1]
            if adj[u]:
                v = adj[u].pop()
                stack.append(v)
            else:
                path.append(u)
                stack.pop()

        path = path[::-1]
        res = []


        for i in range(len(path)-1):
            res.append([path[i], path[i+1]])
        
        return res




        

