import random
from hashtable.hashtable import HashTableEntry, BucketList, HashTable
# from hashtable import HashTableEntry, BucketList, HashTable

word_hashtable = HashTableEntry(6)


# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here

# Create list in
word_linkedlist = BucketList()
split_words = words.split()
split_words.reverse()
print(split_words)

for word in split_words:
    if word is not None:

        word_linkedlist.add_to_head(None, word)


# Feed linked list into hashtable
start_words = HashTable(6)
regular_words = HashTable(6)
end_words = HashTable(6)
current_word = word_linkedlist.head
prev_word = None

step = 1
while step < word_linkedlist.count:
    if prev_word is None:
        if start_words.g
        start_words.put(current_word.value, [current_word.next.value])

        # TODO: construct 5 random sentences
        # Your code here


print(len(split_words))
print(word_linkedlist.count)
print(word_linkedlist.head.value)
print(word_linkedlist.head.next.value)
