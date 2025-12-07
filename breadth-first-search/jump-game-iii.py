from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        #Build graph

        n = len(arr)

        def inBounds(i):
            return i >= 0 and i < n
        
        queue = deque([start])
        visited = { start }
        

        while queue:
            idx = queue.popleft()
            val = arr[idx]
            if arr[idx] == 0:
                return True

            
            l, r = idx - val, idx + val
            if inBounds(l) and l not in visited:
                queue.append(l)
                visited.add(l)
            if inBounds(r) and r not in visited:
                queue.append(r)
                visited.add(r)

        return False




        