"""
Multi-source shortest path.

Converted to DIRECTED graph if needed.
Simpler implementation than runnning Dijkstra's algo over every vertex considered as the source.

"""

class Solution:
    def floydWarshall(self, dist):
        n = len(dist)

        for v in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][v] != int(1e8) and dist[v][j] != int(1e8):
                        dist[i][j] = min(dist[i][j],dist[i][v] + dist[v][j])

        # Negative cycle detection
        for i in range(n):
            if dist[i][i] < 0:
                return "negative cycle detected"