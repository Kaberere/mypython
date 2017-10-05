class WaterBottle:
	def __init__ (self, color, volume, owner, shape):
		self.color = color
		self.volume = volume
		self.owner = owner
		self.shape = shape

	def isMine(self):
		return self.owner == "Eve"

	def isUnique(self):
		return self.shape == "Sphere"

	def isEmpty(self):
		return self.volume == 0

	def __repr__ (self):
		return """
		WaterBottle
		color = {}
		volume = {}
		owner = {}
		shape = {}
		""".format(self.color, self.volume, self.owner, self.shape)

	def changeVolume(self, newVol):
		self.volume = newVol
		return("The new volume is {}".format(self.volume))

bottle = WaterBottle("Blue", 50, "Eve", "Pyramid")

print(bottle)
print(bottle.isMine())
print(bottle.isUnique())
print(bottle.isEmpty())

