class Person:
	def __init__ (self, name, gender):
		if(name == "Francis"):
			raise ValueError("Horrible Horrible Name")
		else:
			self.__name = name
			self.__gender = gender

totally_not_francis = Person ("Frank", "M")
totally_not_francis.name = "Francis"

def __repr__(self):
	return"This person is a {} named {}" .format(self.__gender, self.__name)

print(totally_not_francis.__dict__)