#| Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.
#| For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.
#| In this example, assume nodes with the same value are the exact same node objects.
#| Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

#-----------------#
# Define Function #
#-----------------#

def find_intersection(headA, headB):
    #| Step 1: Find lengths of both linked lists
    len_A, len_B = 0, 0
    current_A, current_B = headA, headB
    
    while current_A is not None:
        len_A += 1
        current_A = current_A.next
    
    while current_B is not None:
        len_B += 1
        current_B = current_B.next
    
    #| Step 2: Move the pointer of the longer list to make them equidistant
    current_A, current_B = headA, headB
    while len_A > len_B:
        current_A = current_A.next
        len_A -= 1
    
    while len_B > len_A:
        current_B = current_B.next
        len_B -= 1
    
    #| Step 3: Move both pointers until they meet (intersection point)
    while current_A is not None and current_B is not None:
        if current_A == current_B:
            return current_A  # Intersection node found
        
        current_A = current_A.next
        current_B = current_B.next
    
    return None  # No intersection found

#------------------#
# Test Applciation #
#------------------#

#| Construct the example linked lists
A = ListNode(3, ListNode(7, ListNode(8, ListNode(10))))
B = ListNode(99, ListNode(1, A.next.next))  # intersect at A's 8

#| Find the intersection node
intersection_node = find_intersection(A, B)

if intersection_node:
    print("Intersection node value:", intersection_node.value)
else:
    print("No intersection found")
