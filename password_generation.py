import random 
MAX_LEN = 12
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',  
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
                     'z']
UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',  
                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
                     'Z'] 
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',  
           '*', '(', ')', '<', '&']
COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

rand_digit = random.choice(DIGITS)
rand_upper = random.choice(UPCASE_CHARACTERS)
rand_lower = random.choice(LOCASE_CHARACTERS)
rand_symbol = random.choice(SYMBOLS)

#print(rand_digit)
#print(rand_upper)
#print(rand_lower)
#print(rand_symbol)

temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
#print(temp_pass)

for i in range(0,(MAX_LEN - 4)):
	temp_pass = temp_pass + random.choice(COMBINED_LIST)
#print(temp_pass)

temp_pass_list = [s + '' for s in temp_pass]
#print(temp_pass_list)
random.shuffle(temp_pass_list)
#print(temp_pass_list)

password = ''
for x in temp_pass_list:
	password = password + x

print(password)
print(type(password))
