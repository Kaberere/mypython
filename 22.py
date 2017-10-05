word = "learN Python The hArd Way"
words = word.lower()
worded = words.split(" ")
newstr = []
for wo in worded:
	newstr.append(wo.capitalize())
	# newstr.append (word)
print(" ".join(newstr))
words = ("" .join(newstr))