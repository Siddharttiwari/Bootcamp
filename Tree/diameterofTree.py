class Node:
    def __init__(self,data=0,left=None,right=None):
        self.data=data
        self.right=right
        self.left=left
def treeInput():
    rootData=int(input())
    if rootData ==-1:
        return 
    root=Node(rootData)
    leftside=treeInput()
    rightside=treeInput()
    root.left=leftside
    root.right=rightside
    return root

def diameter(root):
    maxi=0
    if root is None:
        return 0
    LF=diameter(root.left)
    RH=diameter(root.right)
    maxi=max(maxi,LF+RH)
    return 1+max(LF,RH)
def printTree(root):
    if root ==None:
        return
    print(root.data,end=":")
    if root.left!=None:
        print("L",root.left.data,end=",")
    if root.right!=None:
        print("R",root.right.data,end=",")
    print()
    printTree(root.left)
    printTree(root.right)

root=treeInput()
printTree(root)
diameter(root)