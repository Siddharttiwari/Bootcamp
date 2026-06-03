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
        print(head.data ,end=" ")
        head=head.next
    print("None")
    return

def removeduplicate(head):
    if head is None:
        return head

    seen = set()
    curr = head
    prev = None

    while curr:
        if curr.data in seen:
            prev.next = curr.next
        else:
            seen.add(curr.data)
            prev = curr

        curr = curr.next

    return head

head=takeinput()
printll(head)
head=removeduplicate(head)
printll(head)