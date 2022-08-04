### Simple Number Guessing game ###

import random

playerName = input("Hey there, what\'s your name?")
welcomeMessage = print("Thanks " + playerName.title() + "! The game will begin shortly!")

playerLife = 5

correctAnswer = random.randint(0, 101)

playerAnswer = input("Please key in a number between 1 to 100: ")

while playerLife > 0:
	if int(playerAnswer) < correctAnswer:
		playerLife -= 1
		if playerLife == 0:
			print ("Aw you were so close! The correct number is " + str(correctAnswer) + ".\nBetter luck next time!")
			break
		else:
			playerAnswer = input("Aw that's too low! \nLife left: " + str(playerLife) +"\nGuess again mate: ")

	elif int(playerAnswer) > correctAnswer:
		playerLife -= 1
		if playerLife == 0:
			print ("Aw you were so close! The correct number is " + str(correctAnswer) + ".\nBetter luck next time!")
			break
		else:
			playerAnswer = input("That's too high! \nLife left: " + str(playerLife) +"\nGuess again mate: ")

	elif int(playerAnswer) == correctAnswer:
		print('DING DING DING WE HAVE A WINNER!!!!\nCongratulations you won the game!!!')
		break


	
