
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
def evenodd(head):
    curr=head
    even=[]
    odd=[]
    while curr is not None:
        if curr.data%2==0:
            even.append(curr.data)
        else:
            odd.append(curr.data)
        curr=curr.next
    even.reverse()
    odd.reverse()
    value=even+odd

    new_head=None
    tail=None
    for val in value:
        newNode=Node(val)

        if new_head is None:
            new_head=newNode
            tail=newNode
        else:
            tail.next=newNode
            tail=newNode
    return new_head

"""

def evenodd(head):
    if head is None or head.next is None:
        return head
    evenhead=eventail=None
    oddhead=oddtail=None
    curr=head
    while curr:
        if curr.data%2==0:
            if not evenhead:
                evenhead=eventail=curr
            else:
                eventail.next=curr
                eventail=curr
        else:
            if not oddhead:
                oddhead=oddtail=curr
            else:
                oddtail.next=curr
                oddtail=curr
        curr=curr.next
    if not evenhead:
        return oddhead
    if not oddhead:
        return evenhead
    eventail.next=oddhead
    oddtail.next=None
    return evenhead


head=takeinput()
printll(head)
head=evenodd(head)
printll(head)


