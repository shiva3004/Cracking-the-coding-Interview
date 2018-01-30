from LinkedList import LinkedList


def remove_dups(ll):
   tail = prev = ll.head
   does_contain = set([])
   while tail is not None:
       if tail.value in does_contain:
           prev.next = tail.next
       else:
           does_contain.add(tail.value)
           prev = tail
       tail = tail.next
   return ll





ll = LinkedList()
ll.generate(100, 0, 9)
print(ll)
remove_dups(ll)
print(ll)

ll.generate(100, 0, 9)
print(ll)
