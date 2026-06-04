class Node:
     def __init__(self,data):
          self.data=data
          self.next=None
def takeinput():
     inputlist=[int (ele) for ele in input().split()]
     head=None
     tail=None
     for currdata in inputlist:
          if currdata==-1:
               break
          newNode=Node(currdata)
          if head is None:
               head =newNode
               tail=newNode
          else:
               tail.next=newNode
               tail=newNode
     return head
def printll(head):
     while head is not None:
          print(head.data,end=" ")
          head=head.next
     return
          
def detectCycle(head):
        slow = head
        fast = head

        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:

                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                return slow

        return None

head=takeinput()
printll(head)
head=detectCycle(head)
printll(head)