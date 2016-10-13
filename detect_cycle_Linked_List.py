"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
            
"""

def has_cycle(head):
    sptr = fptr = head
    if head is None:
        return False
    else:
        while (sptr and fptr and fptr.next):
            sptr = sptr.next
            fptr = fptr.next
            if sptr == fptr:
                return True
                break
        return False
        