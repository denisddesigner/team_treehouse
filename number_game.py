import random


def game():

# generate a random number between 1 and 10
	secret_number = random.randint(1, 10)
	guesses = []

	while len(guesses) < 5:
		try:
		# get a number guess from the player
			guess = int(input("Guess a number between 1 and 10: "))
		except ValueError:
			print("{} isn't a number.".format(guess))
		# compare guess to secret number
		else:
			if guess == secret_number:
				print("You got it! My number was {}".format(secret_number))
				break
			elif guess < secret_number:
				print("My number is greater than {}".format(guess))
			elif guess > secret_number:
				print("My number is lower than {}".format(guess))
		# print hit/miss
			else:
				print("That's not it!")
			guesses.append(guess)
	else:
		print("You didn't get it! My number was {}".format(secret_number))
	play_again = input("Do you want to play again? Y/n ")
	if play_again.lower() != 'n':
		game()
	else:
		print("Bye!")
		
game()
