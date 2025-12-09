import heapq
import math

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = { i:[] for i in range(1, n+1)}

        for s,d,t in times:
            graph[s].append((d, t))

        delay = {}
        for i in range(1, n+1):
            delay[i] = math.inf
        visited = { k }

        heap = [(0,k)]
        heapq.heapify(heap)

        while heap:
            d, i = heapq.heappop(heap)
            if d < delay[i]:
                delay[i] = d
            
            visited.add(i)
            for j, dist in graph[i]:
                if j not in visited:
                    heapq.heappush(heap, (d+dist, j))

        res = max(delay.values())
        
        if res == math.inf:
            return -1
        return res

        