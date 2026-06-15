class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
        
def Inorder(root):
    if root is None:
        return 0
    Inorder(root.left)
    print(root.data)
    Inorder(root.right)


def treeinput():
    rootData=int(input())
    if rootData ==-1:
        return None
    root=Node(rootData)
    leftTree=treeinput()
    rightTree=treeinput()
    root.left=leftTree
    root.right=rightTree
    return root

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
root=treeinput()
printTree(root)
print("Inorder Traversal:")
Inorder(root)