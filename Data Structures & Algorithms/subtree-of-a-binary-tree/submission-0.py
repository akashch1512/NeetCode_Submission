# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if not p and not q:
                return True

            if not p or not q:
                return False

            if p.val != q.val:
                return False

            return (isSameTree(p.left, q.left) and
                    isSameTree(p.right, q.right))
        
        stack = [root]
        node = root
        sub = subRoot

        while stack:
            node = stack.pop()

            if node.val == subRoot.val and isSameTree(node, subRoot):
                return True

            if node.right:
                stack.append(node.right)
            
            if node.left:
                stack.append(node.left)
        
        return False