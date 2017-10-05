word = 'QPVWQOVWQLVWQIVWQCVWQEV'
results = ""
for key, character in enumerate(word):
	if word [key - 1] == 'Q' and word [key + 1] == 'V':
		results+=character
print(results)
