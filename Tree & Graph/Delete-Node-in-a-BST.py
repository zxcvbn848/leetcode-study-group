
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:    
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root

        else:
            smallestNodeInRight = self.findSmallest(root.right)
    
            if not smallestNodeInRight:   
                return root.left

            smallestNodeInRight.left = root.left

            return root.right

    def findSmallest(self, root):
        if not root:   
            return None

        while root.left:
            root = root.left

        return root