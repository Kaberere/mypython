words = {"the":"t-word", "and":"a-word", "cow":"c-word", "barn":"b-word"}
input = "The dogs and cows were at the barn"
inputt = input.lower().split(" ")
for index, val in enumerate(inputt):
	if val in words:
		inputt[index] = words[val]
output = " ".join(inputt)
print(output)