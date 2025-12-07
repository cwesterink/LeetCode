from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        #Build graph

        n = len(arr)

        def inBounds(i):
            return i >= 0 and i < n
        
        queue = deque([start])
        visited = set()
        

        while len(queue) > 0:
            frontier = []
            for i in range(len(queue)):
                idx = queue.popleft()
                val = arr[idx]
                if arr[idx] == 0:
                    return True

                visited.add(idx)
                l, r = idx - val, idx + val
                if inBounds(l) and l not in visited:
                    queue.append(l)
                if inBounds(r) and r not in visited:
                    queue.append(r)

        return False




        