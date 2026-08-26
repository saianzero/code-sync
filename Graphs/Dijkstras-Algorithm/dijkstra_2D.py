from typing import List
import heapq

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        if m == 0 or n == 0 or grid[0][0] != 0:
            return -1

        directions = [
            (1, 1), (0, 1), (1, 0), (0, -1),
            (-1, 0), (-1, -1), (1, -1), (-1, 1)
        ]

        result = [[float("inf")] * n for _ in range(m)]

        # (distance, x, y)
        min_heap = [(0, 0, 0)]
        result[0][0] = 0

        while min_heap:
            d, x, y = heapq.heappop(min_heap)

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                if (
                    0 <= nx < m and
                    0 <= ny < n and
                    grid[nx][ny] == 0 and
                    d + 1 < result[nx][ny]
                ):
                    heapq.heappush(min_heap, (d + 1, nx, ny))

                    grid[nx][ny] = 1
                    result[nx][ny] = d + 1

        if result[m - 1][n - 1] == float("inf"):
            return -1

        return result[m - 1][n - 1] + 1