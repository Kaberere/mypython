class Person:
	def __init__ (self, name, gender):
		if(name == "Francis"):
			raise ValueError("Horrible Horrible Name")
		else:
			self.name = name
			self.gender = gender

totally_not_francis = Person ("Frank", "M")
totally_not_francis.name = "Francis"

print(totally_not_francis.name)