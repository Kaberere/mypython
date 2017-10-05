def say_a_lot(*args):
	print("I like: ")
	for word in args:
		print(str(word) + "")
	print("a lot")
say_a_lot("Cows", "Pigs", "MEST", 18)
say_a_lot("Francis & his glasses")