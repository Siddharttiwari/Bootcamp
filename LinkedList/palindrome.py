class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None

def takeinput():
    inputlist=[int (el) for el in input().split()]
    head=None
    tail=None
    for curr in inputlist:
        if curr==-1:
            break
        newNode=Node(curr)
        if head is None:
            head=newNode
            tail=newNode
        else:
            tail.next=newNode
            tail=newNode
    return head

def printll(head):
    while head is not None:
        print(head.data,end="")
        head=head.next
    print("None")
    return
        

"""
def palindrome(head):
    stack=[]
    temp=head
    while temp is not None:
        stack.append(temp.data)
        temp=temp.next
    temp=head
    while temp is not None:
        if temp.data!=stack[-1]:
            return False
        temp=temp.next
        stack.pop()
    return True

    """
def reversed(head):
    if head is None or head.next is None:
        return head  

   
    new_head = reversed(head.next)

    
    front = head.next

   
    front.next = head

    
    head.next = None

    return new_head

def palindrome(head):
    slow=head
    fast=head
    while fast.next and fast.next.next is not None:
        slow=slow.next
        fast=fast.next.next
        
        newhead=reversed(slow.next)
        first=head
        second=newhead
        while(second is not None):
            if (first.data)!=second.data:
                reversed(newhead)
                return False
            first=first.next
            second=second.next
        reversed(newhead)
        return True

head = takeinput()

printll(head)

if palindrome(head):
    print("Palindrome")
else:
    print("Not a Palindrome")