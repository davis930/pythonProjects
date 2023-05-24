from pprint import pprint
sentence = "This is a common interview question"

char_sequence = {}
for char in sentence:
    if char in char_sequence:
        char_sequence[char] += 1
    else:
        char_sequence[char] = 1

char_sequence_sorted = (sorted(char_sequence.items(), key=lambda kv:kv[1], reverse= True))
print(char_sequence_sorted[0])
