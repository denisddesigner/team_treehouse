BIRTHDAYS = (

	("James", "9/8", True, 9),
	("Shawna", "12/6", True, 22),
	("Amaya", "28/2", False, 8),
	("Sam", "16/7", False, 22),
	("Xan", "14/3", False, 34),

	)

# Problem 1: Birthdays
# Loop through all the people in Birthdays, if they have a birthday print out "Happy Birthday" and their name

for person in BIRTHDAYS:
	if person[2] == True:
		print("Happy Birthday " + person[0])

# Problem 2: Half Birthdays
# Loop through all the people in Birthdays and print out their name and half birthdays

for person in BIRTHDAYS:
	print(person[1] + str(6))

# Problem 3: School Year Birthdays
# If their birthday is between September and June print out their name


# Problem 4: Wishing Stars
# Loop through Birthdays
# If the person celebrates their birthday and their age is 10 or less
# Print out their age and the amount of stars for their age

for person in BIRTHDAYS:
	if person[2] == True and person[3] < 10:
		print("Stars: " +  "" + str(person[3]))


