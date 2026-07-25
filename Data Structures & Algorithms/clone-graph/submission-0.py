"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque
from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        clone = {}
        clone[node] = Node(node.val)

        q = deque([node])

        while q:
            t = q.popleft()

            for i in t.neighbors:

                if i not in clone:
                    clone[i] = Node(i.val)
                    q.append(i)

                clone[t].neighbors.append(clone[i])

        return clone[node]