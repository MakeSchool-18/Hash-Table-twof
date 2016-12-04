from linked_list import Linked_List


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size"""
        self.buckets = [Linked_List() for i in range(init_size)]

    def __repr__(self):
        """Return a string representation of this hash table"""
        return 'HashTable({})'.format(self.length())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored"""
        return hash(key) % len(self.buckets)

    def length(self):
        """Return the length of this hash table by traversing its buckets"""
        total = 0

        for list in self.buckets:
            total += list.length()

        return total

    def contains(self, key):
        """Return True if this hash table contains the given key, or False"""
        bucket = self.buckets[self._bucket_index(key)]

        if bucket.find(lambda item: item[0] == key) is not None:
            return True
        else:
            return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError"""
        bucket = self.buckets[self._bucket_index(key)]
        found_item = bucket.find(lambda item: item[0] == key)

        if found_item is not None:
            return found_item[1]
        else:
            raise KeyError

    def set(self, key, value):
        """Insert or update the given key with its associated value"""
        bucket = self.buckets[self._bucket_index(key)]
        bucket.upsert_first([key, value], lambda item: item[0] == key)

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError"""
        bucket = self.buckets[self._bucket_index(key)]

        try:
            bucket.delete(key, lambda item: item[0] == key)
        except ValueError as e:
            raise KeyError

    def keys(self):
        """Return a list of all keys in this hash table"""
        key_list = []

        for bucket in self.buckets:
            bucket_list = bucket.as_list(lambda data: data[0])
            key_list.extend(bucket_list)

        return key_list

    def values(self):
        """Return a list of all values in this hash table"""
        val_list = []

        for bucket in self.buckets:
            bucket_list = bucket.as_list(lambda data: data[1])
            val_list.extend(bucket_list)

        return val_list
