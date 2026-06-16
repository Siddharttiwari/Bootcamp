class Solution:
    def isBalanced(self, root): 
        if root is None:
            return True
        
        left_height = 0
        right_height = 0
        
        if root.left:
            left_height = self.maxDepth(root.left)
        
        if root.right:
            right_height = self.maxDepth(root.right)
        
        if abs(left_height - right_height) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def maxDepth(self, root):
        if root is None:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))