
from linked_list import Linked_List
from hashtable import HashTable
#
ll = Linked_List()

ll.upsert_first(["hello", 1], lambda item: item[0] == "hello")
# ll.upsert_first(["world", 2], lambda item: item[0] == "world")
# ll.upsert_first(["dog", 4], lambda item: item[0] == "dog")

print(ll.as_list())

ll.upsert_first(["hello", 3], lambda item: item[0] == "hello")
# ll.upsert_first(["world", 3], lambda item: item[0] == "world")
# ll.upsert_first(["dog", 10], lambda item: item[0] == "dog")

print(ll.as_list())

# ht = HashTable()
# ht.set('I', 1)
# ht.set('V', 4)
# ht.set('X', 9)
#
# print(ht.keys())
# print(ht.values())
#
# ht.set('V', 5)  # Update value
# ht.set('X', 10)  # Update value
#
# print(ht.keys())
# print(ht.values())
