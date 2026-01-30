from collections import deque
# LC-662 : Find the max width in a binary tree

# nodes index -> if you are at 0 -> idx(right) == 2 ** idx + 1 | idx(left) == 2 ** idx + 2 | width at level = index(q.front()) - index(q.back()) + 1 -> this is the whole idea
   
# solution :
    # -> perform bfs with (nodes, index)
    # -> width at level = index(q.front()) - index(q.back()) + 1

class Solution:
    def bfs(self,root):
        q = deque()
        q.append((root, 0))
        while q:
            front, idxf = q[0]
            rear, idxr = q[-1]

            self.width = max(self.width, idxr - idxf + 1)
            for _ in range(len(q)):
                node, idx = q.popleft()
                if node.left:
                    q.append((node.left, 2 * idx + 1))
                
                if node.right:
                    q.append((node.right, 2 * idx + 2))
                    

    def widthOfBinaryTree(self, root) -> int:
        self.width = 0
        self.bfs(root)
        return self.width