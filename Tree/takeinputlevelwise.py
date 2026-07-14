from collections import deque
class Node:
    def __init__(self,data=0,right=None,left=None):
        self.data=data
        self.right=right
        self.left=left
        
def takeinputLevelwise():
    rootdata=int(input())
    if rootdata==-1:
        return None
    root=Node(rootdata)
    q=deque([root])
    while q:
        current=q.popleft()
        leftdata=int(input())
        if leftdata!=-1:
            current.left=Node(leftdata)
            q.append(current.left)
        rightdata=int(input())
        if rightdata!=-1:
            current.right=Node(rightdata)
            q.append(current.right)
    return root
    
def printtree(root):
    if root is None:
        return 
    print(root.data,end=":")
    if root.left:
        print("L", root.left.data, end=" ")
    if root.right:
        print("R", root.right.data, end=" ")
    print()

    printtree(root.left)
    printtree(root.right)

root = takeinputLevelwise()
printtree(root)