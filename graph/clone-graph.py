"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None

        frontier = [node]
        created = { node.val: Node(node.val) } # val -> ref
        while len(frontier) > 0:
            x = frontier.pop()
            
            neighbors = []

            for n in x.neighbors:
                
                if n.val not in created:
                    newNeighbor = Node(n.val)
                    created[n.val] = newNeighbor
                    frontier.append(n)
                    neighbors.append(newNeighbor)
                else:
                    neighbors.append(created[n.val])
            created[x.val].neighbors = neighbors

        print(created[node.val])
        return created[node.val]
        