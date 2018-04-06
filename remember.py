def rememberer(thing):

	#open file
	with open("database.txt", "a") as file:
		#write thing to file
		file.write(thing+"\n")
		

if __name__  == '__main__':
	rememberer(input("What should I remember? "))