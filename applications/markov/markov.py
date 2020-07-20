import random
from hashtable.hashtable import HashTableEntry, BucketList, HashTable
# from hashtable import HashTableEntry, BucketList, HashTable

word_hashtable = HashTableEntry(6)
end_punctuation = ['.', '?', '!', '."', '?"', '!"']


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
        # if end word

        # if start word
        word_linkedlist.add_to_head(None, word)


# Feed linked list into hashtable
start_words = dict()
regular_words = dict()
end_words = dict()
current_word = word_linkedlist.head
prev_word = None


step = 0
while step < word_linkedlist.count:
    end_check = [current_word.value[-2:], current_word[-1:]]
    # if start word
    if prev_word is None:
        if current_word.value in start_words:
            start_words[current_word.value] = start_words[current_word.value].append(
                current_word.next.value)
        else:
            start_words[current_word.value] = [current_word.next.value]
        prev_word = current_word

    # if end word

    if any(x in end_punctuation for x in end_check):
        if current_word.value in end_words:
            start_words[current_word.value] = start_words[current_word.value].append(
                current_word.next.value)
        else:
            end_words[current_word.value] = [current_word.next.value]

            # all other words

    if prev_word is None:

        # TODO: construct 5 random sentences
        # Your code here


print(len(split_words))
print(word_linkedlist.count)
print(word_linkedlist.head.value)
print(word_linkedlist.head.next.value)
