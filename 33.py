word = 'XAYXPYXPYXLYXEY'
results = ""
for key, character in enumerate(word):
	if word [key - 1] == 'X' and word [key + 1] == 'Y':
		results+=character
print(results)
