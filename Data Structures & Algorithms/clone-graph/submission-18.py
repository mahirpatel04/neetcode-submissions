class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        # Pre-populate root node to track visited status immediately
        oldToNew = {node: Node(node.val)}
        q = deque([node])

        while q:
            curr = q.popleft()
            for n in curr.neighbors:
                if n not in oldToNew:
                    oldToNew[n] = Node(n.val)
                    q.append(n)
                oldToNew[curr].neighbors.append(oldToNew[n])

        return oldToNew[node]