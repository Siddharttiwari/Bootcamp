class Node:
    def __init__(self,data=0,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

def treeInput():
    rootData=int(input())
    if rootData==-1:
        return 
    root=Node(rootData)
    leftside=treeInput()
    rightside=treeInput()
    root.left=leftside
    root.right=rightside
    return root

def printtree(root):
    if root ==-1:
        return
    print(root.data)
    if root.left!=None:
        print(root.left.data)
    elif root.right!=None:
        print(root.right.data)
    print()
    print(root.left)
    print(root.right)
maxi=0
def depth(root):
    global maxi
    if root is None:
        return 0
    LF=depth(root.left)
    RH=depth(root.right)
    
    maxi=max(maxi,LF+RH+root.data)

    return max(LF,RH)+root.data


