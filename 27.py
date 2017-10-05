words = {'a':'q', 'e':'z', 'q':'a', 'z':'e', 't':'m', 'm':'t', 'w':'n', 'n':'w', 'o':'r', 'r':'o', 'l':'s', 's':'l'}
input = "Nobody will ever guess what I'm saying"
inputt = input.upper().split(" ")
for index, val in enumerate(inputt):
	if val in words:
		inputt[index] = words[val]
output = " ".join(inputt)
print(output)