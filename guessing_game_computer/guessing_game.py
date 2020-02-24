#Guessing game which includes computer guessing the number user is thinking of. Once the computer answers correctly, print out number of tries it took computer to guess user's number

import random

lower_limit = 0
upper_limit = 101

array_of_previously_guessed = []

guess_counter = 0 

print("User think of a number 1-100 and remember it!")

while True : 
	computer_guess = random.randint(lower_limit,upper_limit)
	print("Computer's guess : " +str(computer_guess))

	user_response = str(input("User, how was my guess?"))

	if(user_response != 'low' and user_response != 'high' and user_response != 'correct') :
		print('Please input "low" or "high"\n')
		break

	if(user_response == 'high'):
		array_of_previously_guessed.append(computer_guess)
		lower_limit = lower_limit
		upper_limit = computer_guess-1
		guess_counter += 1
		continue
		
	if(user_response == 'low') : 
		array_of_previously_guessed.append(computer_guess)
		lower_limit = computer_guess+1
		upper_limit = upper_limit	
		guess_counter += 1
		continue
	
	
	if(user_response == 'correct'):
		print("\nYay, I guessed correctly!")
		print("\nIt took me " +str(guess_counter)+ " guesses")
		break



