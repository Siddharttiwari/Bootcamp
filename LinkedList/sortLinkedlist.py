def sortLL(head):
        arr=[]
        temp=head
        while temp is not None:
            arr.append(temp.data)
            temp=temp.next
        arr.sort()
        temp=head
        for val in arr:
            temp.data=val
            temp=temp.next
        return head