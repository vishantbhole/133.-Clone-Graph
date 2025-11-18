
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



def serialize_graph(start: Optional[Node]) -> List[List[int]]:
    # Helper to print something meaningful: return adjacency list from the cloned graph
    if not start:
        return []
    from collections import deque
    idmap = {}
    order = []
    q = deque([start])
    idmap[start] = start.val
    seen = {start}
    while q:
        u = q.popleft()
        order.append(u)
        for v in u.neighbors:
            if v not in seen:
                seen.add(v)
                q.append(v)
    n = max(node.val for node in order)
    adj = [[] for _ in range(n)]
    for u in order:
        adj[u.val-1] = [v.val for v in u.neighbors]
    return adj



if __name__ == "__main__":
    sol = Solution()

    # Example 1
    adjList = [[2,4],[1,3],[2,4],[1,3]]
    graph1 = build_graph_from_adj_list(adjList)
    clone1 = sol.cloneGraph(graph1)
    print("Cloned adj list 1:", serialize_graph(clone1))

    # Example 2 (single node, no edges per LeetCode format: [[]])
    adjList2 = [[]]
    graph2 = build_graph_from_adj_list(adjList2)
    clone2 = sol.cloneGraph(graph2)
    print("Cloned adj list 2:", serialize_graph(clone2))

