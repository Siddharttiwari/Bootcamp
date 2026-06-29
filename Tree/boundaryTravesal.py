class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None    
        
    def isleaf(self,root):
                return not root.left and not root.right
                
    def addleft(self,root,res):
        curr=root.left
        while curr:
            if not self.isleaf(curr):
                res.append(curr.data)
            if curr.left:
                curr=curr.left
            else:
                curr=curr.right
                
    def addright(self,root,res):
        curr=root.right
        temp=[]
        while curr:
            if not self.isleaf(curr):
                temp.append(curr.data)
            if curr.right:
                curr=curr.right
            else:
                curr=curr.left
        for i in range(len(temp)-1,-1,-1):
            res.append(temp[i])
    
    def addleaves(self,root,res):
        if self.isleaf(root):
            res.append(root.data)
            return
        if root.left:
            self.addleaves(root.left,res)
        if root.right:
            self.addleaves(root.right,res)
        
                
    def boundaryTraversal(self, root):
        res=[]
        if not root:
            return res
        if not self.isleaf(root):
            res.append(root.data)
        
        self.addleft(root,res)
        self.addleaves(root,res)
        self.addright(root,res)
        
        return res
    