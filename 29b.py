text = 'The quick brown fox jumps over the lazy fox'
words = text.lower().split()
wordDict = {}
for word in words:
	if word in wordDict:
		wordDict[word]+=1
	else:
		wordDict[word]=1
print(wordDict)