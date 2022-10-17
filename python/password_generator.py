'''

@author: Ayush Shete

'''


import itertools as it
import random
import pyperclip 


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

## Welcoming
print(bcolors.OKBLUE + "Starting Password Generator...")
print("")

characters = {
    "Uppercases": ['ABCDEFGHIJKLMNOPQRSTUVWXYZ'],
    "Lowercases": ['abcdefghijklmnopqyrstuvwxyz'],
    "Numbers": ['0123456789'],
    "Symbols": ['!@#$&*?_-'],
}

while True:
    try:
        n = int(input("\tLength of Password: "))
        break
    except ValueError:
        print(bcolors.FAIL + "Entered Value should be integer only")
        print("Restarting the program...")
        print(bcolors.OKBLUE + "")
        pass

def gen_pass(n):
    print(bcolors.OKGREEN + "Select Character type number from the list: ")
    arr = ["Numbers", "Uppercases", "Lowercases", "Symbols"]
    l1 = list(it.combinations(arr, 1))
    l2 = list(it.combinations(arr, 2))
    l3 = list(it.combinations(arr, 3))
    l4 = list(it.combinations(arr, 4))
    l = l1 + l2 + l3 + l4  # list of all the possible combinations of characters
    for i in range(len(l)):
        print("\t",i+1, " --- ", l[i])
    print(bcolors.OKBLUE + "")
    while True:
        c_type = int(input("Type any serial number from the above list of combinations: "))
        if c_type in range(1, 16):
            break
        else:
            print(bcolors.HEADER + "Serial number should be from 1 to 15...")
            print(bcolors.OKBLUE + "")        
     
     ## Generating password with selected combination
    s_comb_l = [i for i in list(l[c_type - 1])] # selected character combination list
    print(s_comb_l)
    c_per_pass = n // len(s_comb_l)
    extra_c = n - (c_per_pass * len(s_comb_l))
    password_l = []
    all_char = []
    for i in range(0, len(s_comb_l)):
        x = s_comb_l[i]
        z = characters[x][0]
        l = [char for char in z]
        all_char.extend(l)
        c =  random.choices(l, k = c_per_pass)
        password_l.extend(c)
    e_c = random.choices(all_char, k = extra_c)
    password_l.extend(e_c)
    random.shuffle(password_l)
    password = "".join(password_l) 
    print(bcolors.HEADER+ "Your password: ", password)
    pyperclip.copy(password)
    print(bcolors.OKCYAN+ "Your password is copied to your clipboard.")


gen_pass(n)