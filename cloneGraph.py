
#133. Clone Graph
from typing import Optional, List, Dict

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
    def __repr__(self):
        return f"Node({self.val})"

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew: Dict[Node, Node] = {}
        def dfs(n: 'Node') -> 'Node':
            if n in oldToNew:
                return oldToNew[n]
            copy = Node(n.val)
            oldToNew[n] = copy
            for nei in n.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None
