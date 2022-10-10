import random
import string
import array

print('Welcome to Password generator!')
MAX_LEN = 12
LOCASE_CHARACTERS = string.ascii_lowercase
UPCASE_CHARACTERS = string.ascii_uppercase
DIGITS = string.digits
SYMBOLS = string.punctuation


COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

rand_digit = random.choice(DIGITS)
rand_upper = random.choice(UPCASE_CHARACTERS)
rand_lower = random.choice(LOCASE_CHARACTERS)
rand_symbol = random.choice(SYMBOLS)

temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

for x in range(MAX_LEN - 4):
	temp_pass = temp_pass + random.choice(COMBINED_LIST)
	temp_pass_list = array.array('u', temp_pass)
	random.shuffle(temp_pass_list)

password = ""
for x in temp_pass_list:
		password = password + x
		
print(password)
