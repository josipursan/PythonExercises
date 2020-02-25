#Make a hangman game

import random

hangman_positions = ['''
- - - - + 			
|	
0				
		
		
		
======= ''', '''
- - - - + 			
|		
0				
|		
		
		
========= ''', '''

 - - - + 			
 |		
 0				
/|		
		
		
========= ''', '''

   - - - + 			
   |	
   0			
  /|\
		
		
========= ''', '''

  - - - + 			
  |		
  0				
 /|\	
 / 	    
		
========= ''', '''

   - - - + 			
   |	
   0			
  /|\	
  / \	
		
========= ''']


word_count = 0
array_for_guessing = []
counter_for_hangman_positions = 0

file_to_open = "words.txt"
f = open(file_to_open)
f.seek(0)

word = f.readlines()
f.close()

for element in word : 
	word_count += 1

random_num_to_choose_a_word = random.randint(0,word_count-1)

print("Word : " +str(word[random_num_to_choose_a_word]))

chosen_word_split = list(word[random_num_to_choose_a_word])	#quickly split a string 
del chosen_word_split[len(chosen_word_split)-1]	#for deleting \n element in chosen_word_split array
print("Chosen word split : " +str(chosen_word_split))

for element in range(0, len(chosen_word_split)) :
	array_for_guessing.append('_')

print("User, the word I'm thinking of has " +str(len(chosen_word_split))+ " letters")

while True : 
	user_guess_letter = str(input("\nUser, guess a letter : "))

	if(user_guess_letter not in chosen_word_split) :
		print("\nLetter you've chosen is not in the word I'm thinking of!\n")
		counter_for_hangman_positions += 1

		if(counter_for_hangman_positions == 1) : 
			print(hangman_positions[counter_for_hangman_positions-1])
		if(counter_for_hangman_positions == 2) : 
			print(hangman_positions[counter_for_hangman_positions-1])
		if(counter_for_hangman_positions == 3) : 
			print(hangman_positions[counter_for_hangman_positions-1])
		if(counter_for_hangman_positions == 4) : 
			print(hangman_positions[counter_for_hangman_positions-1])
		if(counter_for_hangman_positions == 5) : 
			print(hangman_positions[counter_for_hangman_positions-1])
		if(counter_for_hangman_positions == 6) : 
			print(hangman_positions[counter_for_hangman_positions-1])
			print("You've lost!")
			break
		
		
	else : 	
		for index in range(0, len(chosen_word_split)) : 
			if(user_guess_letter == chosen_word_split[index]) :
				array_for_guessing[index] = user_guess_letter

		print("\nYou guessed a letter right!")
		print("\n" +str(' '.join(array_for_guessing)))

	if(chosen_word_split == array_for_guessing) : 
		print("You guessed the word correctly!")
		break





