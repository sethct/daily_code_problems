#| Given a singly linked list and an integer k, remove the kth last element from the list.
#| k is guaranteed to be smaller than the length of the list.
#| The list is very long, so making more than one pass is prohibitively expensive.
#| Do this in constant space and in one pass.

#------------------#
# Program Fucntion #
#------------------#

#| Initialise list node
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

#| Define function
def remove_kth_from_end(head, k):
    #| If the list is empty, just return None
    if not head:
        return None

    #| Initialise two pointers - both starting at the head of the list
    fast = head
    slow = head

    #| Move the fast pointer k nodes ahead
    for i in range(k):
        fast = fast.next
        #| If fast reaches the end here, remove the head
        if not fast:
            return head.next

    #| Move both pointers until fast reaches the last node
    while fast.next:
        slow = slow.next
        fast = fast.next

    #| At this point, slow is just before the kth node from the end.
    #| Remove the kth node by skipping it
    slow.next = slow.next.next

    #| Return the head of the modified list
    return head

#------------------#
# Test Application #
#------------------#

#| Create linked lists
def create_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

#| Print linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

#| Test the implementation
lst = [1, 2, 3, 4, 5]
head = create_linked_list(lst)
print("Original Linked List:")
print_linked_list(head)

#| Remove the kth last element
k = 2
head = remove_kth_from_end(head, k)
print(f"Linked List after removing {k}th last element:")
print_linked_list(head)
