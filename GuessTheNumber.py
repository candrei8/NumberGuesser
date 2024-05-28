import random 
guesses = 0

def pedir_numero():
	while True : 
		number = input("Enter a number: ")
		if number.isdigit():
			number = int(number)
			if 11 > number > 0  :
				return number
			else: 
				print("Your number has to be grater than 0 and lower than 11")
		else: 
			print("You have to enter a number: ")

while True : 
	guesses += 1
	random_number = random.randint(1,10)
	numero = pedir_numero()
	if numero == random_number : 
		print("Congrats, you have guessed the number in", guesses, "guesses")
		break
	else:
		print("Your number was",numero,"and the bot has chosen",random_number)
	







