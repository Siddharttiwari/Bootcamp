class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
"""
def insertAtI(head,i,data):
    if i<0 :
        return head
    count=0
    prev=None
    curr=head
    while count<i:
        prev=curr
        curr=curr.next
        count=count+1
    if count != i:
        return head
    newNode=Node(data)
    if prev is not None:
        prev.next=newNode
    else:
        head=newNode
    newNode.next=curr
    return head
    """
def takeinput():
    inputlist=[int(el) for el in input().split()]
    head=None
    tail=None

    for currdata in inputlist:
        if currdata==-1:
            break
        newNode=Node(currdata)
        if head is None:
            head=newNode
            tail=newNode
        else:
            tail.next=newNode
            tail=newNode

        
    return head


def insertAti(head,i,data):
    if i<0:
        return head
    if i==0:
        newnode=Node(data)
        newnode.next=head
        return newnode
    if head is None:
        return None
    smallhead=insertAti(head.next,i-1,data)
    head.next=smallhead
    return head
    

def printll(head):
    while head is not None:
        print(str(head.data)+"->",end="")
        head=head.next
    print("None")
    return

head=takeinput()
printll(head)
head=insertAti(head,2,6)
printll(head)
