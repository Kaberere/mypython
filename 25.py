def diamond (height):
	constant = (height*2)+1
	if height % 2 ==0:
		print("Height must be odd")
	else:
		midpoint = int(height/2)+1
	for line in range (1, height+1):
		if line<=midpoint:
			for spaces in range(midpoint-line):
				print(" ", end="")
			for star in range (2* line-1):
				print("*", end="")
	else:
		for spaces in range(line-midpoint):
			print(" ", end="")
		for stars in range(constant-2*line):
			print("*", end="")
	print("")
diamond(5)
diamond(7)