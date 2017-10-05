for i in range(10,51):
	if i%3==0 and i%5==0:
		print("meltwater")
	elif i%3==0:
		print("melt")
	elif i%5==0:
		print("water")
	else:
		print(i)
