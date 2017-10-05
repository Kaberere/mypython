#def wordcount(str):
	#inputt = "The quick brown fox jumps over the lazy fox"
	#input = inputt.lower()
	#counts = dict()
    #words = input.split()

    #for word in words:
        #if word in counts:
            #counts[word] += 1
        #else:
            #counts[word] = 1

    #return counts

#print(input)
text = 'The quick brown fox jumps over the lazy fox'
wordcount = {}
words = text.lower().split()

for word in words:
	counter=0
	for i in range (len(words)):
		if word==words[i]:
			counter+=1
	wordcount[word]=counter
print(wordcount)
