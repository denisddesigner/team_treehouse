sodas = ["Pepsi", "Coke", "Sprite"]
crisps = ["Walkers", "Hunky Doreys"]
candy = ["Snickers", "Mars", "Moro"]

while True:
	choice = input("Would you like a SODA, some CRISPS or a CANDY bar? ").lower()
	try:
		if choice == 'soda':
			snack = sodas.pop()
		elif choice == 'crisps':
			snack = crisps.pop()
		elif choice == 'candy':
			snack = candy.pop()
		else:
			print("Sorry, does not compute!")
			continue
	except IndexError:
		print("Sorry All Out!")

	print("Here's your {} {}".format(choice, snack))