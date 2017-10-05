class Person:
	def __init__(self, name):
		if isinstance(name, str):
			print("Success")
		else:
			raise TypeError("Incorrect")

Eve = Person("Cave")