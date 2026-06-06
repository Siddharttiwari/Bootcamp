zerodummy=Node(-1)
        onedummy=Node(-1)
        twodummy=Node(-1)
        
        zerotail=zerodummy
        onetail=onedummy
        twotail=twodummy
        
        curr=head
        while curr:
            if curr.data==0:
                zerotail.next=curr
                zerotail=zerotail.next
            elif curr.data==1:
                onetail.next=curr
                onetail=onetail.next
            elif curr.data==2:
                twotail.next=curr
                twotail=twotail.next
            curr=curr.next
        zerotail.next=onedummy.next if onedummy.next else twodummy.next
        onetail.next=twodummy.next
        twotail.next=None
        head=zerodummy.next
        return head