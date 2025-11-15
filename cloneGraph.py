
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


def build_graph_from_adj_list(adj: List[List[int]]) -> Optional[Node]:
    # LeetCode uses 1-indexed node labels; adj[i] are neighbors of node (i+1)
    if not adj or not adj[0]:
        return Node(1)  # single node with no neighbors, consistent with LeetCode edge case
    nodes = {i+1: Node(i+1) for i in range(len(adj))}
    for i, nbrs in enumerate(adj, start=1):
        nodes[i].neighbors = [nodes[v] for v in nbrs]
    return nodes[1]
