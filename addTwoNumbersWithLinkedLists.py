#!/usr/bin/env python
# Works in python2 and python3

"""
From Leetcode: https://leetcode.com/problems/add-two-numbers/
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single
digit. Add the two numbers and return it as a linked list. You may assume the two
numbers do not contain any leading zero, except the number 0 itself.
"""

BASE = 10  # Base used for splitting in digits


# Definition for singly-linked list
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        stdout = "({}".format(self.val)
        next = self.next
        while next is not None:
            stdout += " -> {}".format(next.val)
            next = next.next
        stdout += ")"
        return stdout


def create_ListNode_from_number(num):
    # From an int, saves it in digits in a linked list
    tmp = []
    while num > 0:
        tmp.append(num % BASE)
        num = num // BASE
    # Necessary because the digits are stored in reverse (starting from units)
    tmp.reverse()
    next_node = None
    for digit in tmp:
        node = ListNode(digit)
        node.next = next_node
        next_node = node
    # # Uncomment this to make zero and negative numbers be saved as 0 instead of None
    # if next_node is None:
    #     node = ListNode(0)
    return next_node


def get_number_from_ListNode(node):
    # From a ListNode, recover the number
    if node is None:
        return 0
    num = node.val
    i = 0
    while node.next is not None:
        node = node.next
        i += 1
        num = node.val * BASE**i + num
    return num


def add_two_numbers(l1, l2):
    """
    Get 2 linked lists representing two numbers, and return
    another linked list representing their sum

    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    head = ListNode(0)
    idx = head
    carry = 0
    while l1 is not None and l2 is not None:
        total = l1.val + l2.val + carry
        carry = total // BASE
        idx.next = ListNode(total % BASE)
        idx = idx.next
        l1 = l1.next
        l2 = l2.next
    if l1 is not None or l2 is not None:
        # We will only use l1 after this
        if l2 is not None:
            l1 = l2
        while l1 is not None:
            total = l1.val + carry
            carry = total // BASE
            idx.next = ListNode(total % BASE)
            idx = idx.next
            l1 = l1.next
    if carry > 0:
        idx.next = ListNode(carry)
    return head.next


if __name__ == "__main__":
    num1 = 78027
    num2 = 968432
    result = num1 + num2
    print("REGULAR SUM:")
    print(str(num1) + " + " + str(num2) + " = " + str(result))

    n1 = create_ListNode_from_number(num1)
    n2 = create_ListNode_from_number(num2)
    r = add_two_numbers(n1, n2)
    print("\nLINKED LIST SUM:")
    print(str(n1) + " + " + str(n2) + " = " + str(r))

    print("\nREADABLE RESULT: {}".format(get_number_from_ListNode(r)))
