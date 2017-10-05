class Human:
	def __init__ (self, eyecolor, height):
		self.eyecolor = eyecolor
		self.height = height

	def geteyecolor(self):
		print("My eyecolor is {}".format(self.eyecolor))
	
	def seteyecolor(self, eyecolor):
		self.eyecolor = eyecolor
		return self.eyecolor

	def getheight(self):
		print("My height is {}".format(self.height))
	
	def setheight(self, height):
		self.height = height
		return self.height

human = Human('blue', 54)
human.seteyecolor("black")
human.setheight(72)

human.getheight()
human.geteyecolor()
