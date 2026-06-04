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
    return 
def detectLoop(head):
        fast =head
        slow=head
        while fast is not None and fast.next is not None:
            fast=fast.next.next
            slow=slow.next
            if (slow==fast):
                return True
        return False
head = takeinput()

printll(head)
print()

print(detectLoop(head))