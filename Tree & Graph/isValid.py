
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isValid(node, left = float('-inf'), right = float('inf')) -> bool:
            if not node:
                return True

            if node.val <= left or right <= node.val:
                return False

            return (isValid(node.left, left, node.val) and
                    isValid(node.right, node.val, right))

        return isValid(root)