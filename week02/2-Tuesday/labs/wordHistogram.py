def word_count(paragraph):
    word_freq={}
    for word in paragraph.lower().split():
        if word not in word_freq:
            word_freq[word] = 1
        else:
            word_freq[word] += 1
    return word_freq
val = (input('Enter paragraph here: '))
print(word_count(val))
