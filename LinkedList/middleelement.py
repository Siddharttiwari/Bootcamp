
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

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

def printll(head):
    while head is not None:
        print(str(head.data)+"->",end="")
        head=head.next
    print("None")
    return
"""
def getlength(head):
    length=0
    while head:
        length+=1
        head=head.next
    return length

def middle(head):
    length=getlength(head)
    midindex=length//2
    while midindex:
        head=head.next
        midindex-=1
    return head.data
"""

def middle(head):
    slow=head
    fast=head
    while fast is not None and fast.next is not None:
        fast=fast.next.next
        slow=slow.next
    return slow.data
head=takeinput()
printll(head)
head=middle(head)
print(head)


