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
maxi=0
def calculateHeight(root):
    global maxi
    if root is None:
        return 0
    LF=calculateHeight(root.left)
    RH=calculateHeight(root.right)
    maxi=max(maxi,LF+RH)
    return 1+max(LF,RH)

def diameter(root):
        global maxi
        calculateHeight(root)
        return maxi

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