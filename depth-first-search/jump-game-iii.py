from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        #Build graph

        graph = {}
        n = len(arr)

        def inBounds(i):
            return i >= 0 and i < n

        sink = set()
        for i, val in enumerate(arr):
            if val == 0:
                sink.add(i)
                continue
            neighbors = []
            graph[i] = neighbors

            if inBounds(i+val):
                neighbors.append(i+val)
            if inBounds(i-val):
                neighbors.append(i-val)
        
        queue = deque([start])
        visited = set()
        print(graph)
        def getNewNeighbors(i):
            res = []
            for neighbor in graph[i]:
                if neighbor not in visited:
                    res.append(neighbor)
            return res

        while len(queue) > 0:
            frontier = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node in sink:
                    return True

                frontier.extend(getNewNeighbors(node))
                visited.add(node)
            queue.extend(frontier)

        return False




        