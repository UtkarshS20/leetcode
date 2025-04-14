# # Node class
# class Node:
#     def __init__(self, data):
#         self.data = data  # Data part
#         self.next = None  # Pointer to the next node

# # LinkedList class
# class LinkedList:
#     def __init__(self):
#         self.head = None  # Start of the list

#     # Insert at the end
#     def append(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             return
#         temp = self.head
#         while temp.next:
#             temp = temp.next
#         temp.next = new_node

#     # Display the list
#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.data, end=" -> ")
#             temp = temp.next
#         print("None")

# # Example usage
# ll = LinkedList()
# ll.append(10)
# ll.append(20)
# ll.append(30)
# ll.display()  # Output: 10 -> 20 -> 30 -> None

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while list1:
            arr.append(list1.val)
            list1 = list1.next
        
        while list2:
            arr.append(list2.val)
            list2 = list2.next
        if not arr:
            return []
        arr = sorted(arr)
        head = ListNode(arr[0])
        curr = head
        for val in arr[1:]:
            # if not mergedList.next:
            #     mergedList.val = val
            # temp = mergedList.val
            # while temp.next:
            #     temp = temp.next
            # temp.next = mergedList
            # return mergedList
            curr.next = ListNode(val)
            curr = curr.next
        return head
        
# Helper to create linked list from list
def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper to print linked list
def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Test the function
list1 = build_linked_list([1, 3, 5])
list2 = build_linked_list([2, 4, 6])

sol = Solution()
merged = sol.mergeTwoLists(list1, list2)
print_linked_list(merged)
            