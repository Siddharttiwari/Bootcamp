class Node:
    def __init__(self,data=0,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

def treeinput():
    rootData=int(input())
    if rootData is None:
        return
    root=Node(rootData)
    lefttree=treeinput()
    righttree=treeinput()
    root.left=lefttree
    root.right=righttree

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

def postorder(root):
    if root is None:
        return []
    return postorder(root.left)+postorder(root.right)+[root.data]

root=treeinput()
printTree(root)
print("Postorder")
print(postorder(root))