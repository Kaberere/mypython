def diamond (rows, star="*"):
	for row in range (rows):
		space = row * 2 - 1
		if space >= rows - 1:
			space = rows - space % rows - 4
		if space < 1:
			print(star.center(rows))
		else:
			print((star + space * ' ' + star).center(rows))
diamond(5)