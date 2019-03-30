word_dic = {}
text = input("Text: ")
separate_words = text.split()

for word in separate_words:
    frequency = word_dic.get(word, 0)
    word_dic[word] = frequency + 1

separate_words = list(word_dic.keys())
max_length = max((len(word) for word in separate_words))

separate_words.sort()
for word in separate_words:
    print("{:{}} : {}".format(word, max_length, word_dic[word]))