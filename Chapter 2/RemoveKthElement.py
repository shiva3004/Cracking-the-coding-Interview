from LinkedList import LinkedList

def kth_to_last(ll, k):
    head = front = ll.head
    tail = ll.head
    if head is None:
        return head
    for i in range(k):
        tail = tail.next
    while tail is not None:
        tail = tail.next
        front = front.next
    return front





ll = LinkedList()
ll.generate(10, 0, 99)
print(ll)
print(kth_to_last(ll, -1))
