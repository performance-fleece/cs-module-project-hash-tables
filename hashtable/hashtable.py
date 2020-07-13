class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next

    def set_value(self, value):
        self.value = value

    def set_next(self, new_next):
        self.next = new_next

    def __str__(self):
        return f'{self.key}, {self.value}'


class BucketList:
    def __init__(self, count=0):
        self.head = None
        self.count = count

    def add_to_list(self, key, value):
        # if empty add to head
        hashEntry = HashTableEntry(key, value)
        if self.head is None:
            self.count += 1
            self.head = hashEntry

        # if key present, update
        if self.contains(key) is not None:
            self.update(key, value)

        # else, add to head
        else:
            self.add_to_head(key, value)
            self.count += 1

    def update(self, key, value):
        current = self.head
        found = False
        while current is not None:
            if current.key == key:
                current.set_value(value)
                break

            current = current.next

        return found

    def add_to_head(self, key, value):
        hashEntry = HashTableEntry(key, value)
        # bucket NOT empty
        if self.head is not None:
            hashEntry.set_next(self.head)
        # bucket empty
        self.head = hashEntry

    def contains(self, key):
        current = self.head
        found = None
        while current is not None:
            if current.key == key:
                found = current.value
                break

            current = current.next

        return found

    def deleteEntry(self, key):
        tempEntry = self.head
        if self.head.key == key:
            self.head = self.head.next
            self.count -= 1
            return ("head deleted")

        else:
            tempEntry = self.head

            while tempEntry.next is not None:
                if tempEntry.next.key == key:
                    tempEntry.next = tempEntry.next.next
                    self.count -= 1
                    return("deleted")
                tempEntry = tempEntry.next
            return("Key not found")


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity=MIN_CAPACITY):
        # Your code here
        self.capacity = capacity
        self.buckets = [BucketList() for i in range(capacity)]

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.buckets)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for x in key:
            hash = (hash * 33) + ord(x)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        bucket = self.buckets[self.hash_index(key)]

        bucket.add_to_list(key, value)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        bucket = self.buckets[self.hash_index(key)]
        bucket.deleteEntry(key)

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here

        # for k, v in self.buckets[self.hash_index(key)]:
        #     if k == key:
        #         return v
        # return None
        value = self.buckets[self.hash_index(key)].contains(key)
        return value

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
