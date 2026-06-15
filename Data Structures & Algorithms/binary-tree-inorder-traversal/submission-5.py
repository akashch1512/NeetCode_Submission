# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        answer = []

        def recc(root):
            if not root:
                return 
            
            recc(root.left)
            answer.append(root.val)
            recc(root.right)
        
        recc(root)
        return answer
            
