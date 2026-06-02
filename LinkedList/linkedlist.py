class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def takeinput(self):
        inputlist = [int(ele) for ele in input().split()]

        for currData in inputlist:
            if currData == -1:
                break

            newNode = Node(currData)

            if self.head is None:
                self.head = newNode
            else:
                curr = self.head
                while curr.next is not None:
                    curr = curr.next
                curr.next = newNode

    def printll(self):
        curr = self.head
        while curr is not None:
            print(str(curr.data) + "->", end="")
            curr = curr.next
        print("None")

ll = LinkedList()     # object created
ll.takeinput()        # self = ll
ll.printll()          # self = ll