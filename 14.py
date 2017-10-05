def get_squares(*args):
 	squares = []
 	for nums in args:
 		squares.append(nums**2)
 	print(squares)
get_squares(1,3,9,5)
get_squares(13,25)