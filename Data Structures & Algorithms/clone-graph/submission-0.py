"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = dict() # used for record what has been traversed. cycles involved
        def dfs(node : Optional['Node']) ->Optional['Node']:
            if node is None:
                return node
            if oldToNew.get(node, None) is not None:
                copy = oldToNew[node]
                return copy
            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node)



        