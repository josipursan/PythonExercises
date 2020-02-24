#Ask the user how strong would they like their passwords
#Security levels are defined in "array_of_security_parameters"
#Each subarray defines password length and whether numbers and diacritic signs will be used.


import string
import random

def password_generator(password_strength_data) : 

	password = []

	flag_for_numbers = 0
	flag_for_diacritic_signs = 0
	last_level_flag = 0	#used to differentiate between last two security levels which both have same 'y' for numbers and diacritic signs

	#print(password_strength_data)
	
	if(password_strength_data[1] == "y") : 
		flag_for_numbers = 1

	if(password_strength_data[2] == "y") :
		flag_for_diacritic_signs = 1

	if(password_strength_data[3] == "y"):
		last_level_flag = 1

	for element in range(0, password_strength_data[0]) : 
		if(flag_for_diacritic_signs == 1 and flag_for_numbers == 1 and last_level_flag == 1) :   # CASE 3
			password.append(random.choice(string.ascii_letters + string.digits + string.punctuation))

		if(flag_for_numbers == 1 and flag_for_diacritic_signs == 1 and last_level_flag == 0) :		# CASE 2
			password.append(random.choice(string.ascii_letters + string.digits + string.punctuation))

		if(flag_for_numbers == 1 and flag_for_diacritic_signs == 0 and last_level_flag == 0) : 	# CASE 1
			password.append(random.choice(string.ascii_letters + string.digits))

		if(flag_for_numbers == 0 and flag_for_diacritic_signs == 0 and last_level_flag == 0) :		# CASE 0 	
			password.append(random.choice(string.ascii_letters))

	print("Your new password is : " +(' '.join(password)))


def choose_password_strength():

	array_of_security_parameters = [[6,"n","n","n"], [8,"y", "n","n"], [10,"y","y","n"],[14,"y","y","y"]]

	while True : 
		user_choice = int(input("Choose your level of security (1,2,3,4) : "))
		if(user_choice > 0 and user_choice < 5) : 
			break
		else:
			continue

	password_generator(array_of_security_parameters[(user_choice-1)])

################################ ˇˇ MAIN ˇˇ ######################################

choose_password_strength()






#REDOSLIJED PARAMETARA U SVAKOM SECURITY LEVELU : length, numbers (y/n?), diacritic signs(y/n?)    | raspored security levela u array_of_security_parameters : LOW-->MEDIUM-->HIGH-->VERY HIGH

