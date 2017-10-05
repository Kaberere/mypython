text = 'The quick brown fox jumps over the lazy fox'
wordcount = {}
words = text.lower().split()
for word in words:
	if word not in wordcount:
		wordcount[word] = words.count(word)
print(wordcount)