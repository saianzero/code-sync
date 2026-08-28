# https://leetcode.com/problems/network-delay-time/

from collections import defaultdict
import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        res = [float("inf")] * (n+1)
        res[k] = 0

        adj = defaultdict(list)
        for u,v,w in times:
            adj[u].append([v,w])

        min_heap = [[0,k]]

        while min_heap:
            t,u = heapq.heappop(min_heap)

            for v,w in adj[u]:
                if t+w < res[v]:
                    res[v] = t+w
                    heapq.heappush(min_heap, [res[v],v])
        
        if float("inf") in res[1:]:
            return -1
        
        return max(res[1:])


