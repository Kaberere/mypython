class Phone:
	def __init__(self, color, is_on, charge):

		self.color = color
		self.is_on = is_on
		self.charge = charge

	def turn_on():
		self.is_on = True	
	
	def has_charge():
		self.charge = True

	def color():
		self.color = color
		
def main():
	newPhone = Phone("Gold", True, True)
	print(newPhone.color)
	print(newPhone.is_on)
	print(newPhone.charge)

if __name__ == "__main__":
	main()