for line in range(1,4):
    for space in range (3-line):
        print(" " , end="")
    for star in range(2*(line)-1):
        print("*" , end="")
    print("")