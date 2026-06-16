class listnode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def merge_lists(l1,l2):
    dummy = listnode(-1)
    curr = dummy
    while l1 and l2:
        if l1.val <=l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    
    if l1:
        curr.next = l1
    elif l2:
        curr.next = l2
    return dummy.next

def build_ll(values):
    dummy = listnode()
    curr = dummy
    for val in values:
        curr.next = listnode(val)
        curr = curr.next
    return dummy.next

def print_ll(head):
    values = []
    while head:
        values.append(str(head.val))
        head = head.next
        print("-".join(values))

l1 = build_ll([1,2,3,1,5,4,6])
l2 = build_ll([3,4,3,5,4,3,1])
merged_head = merge_lists(l1,l2)
print("merged list")
print_ll(merged_head)
