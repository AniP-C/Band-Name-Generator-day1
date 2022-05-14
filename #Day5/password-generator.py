# import random
# import string
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# password = ""
# # for r_pass in range(1, nr_letters+1):
# #     password= password+ random.choice(letters)

# # for r_pass in range(1, nr_symbols+1):
# #     password= password+ random.choice(symbols)

# # for r_pass in range(1, nr_numbers+1):
# #     password= password+ random.choice(numbers)
# # print(password)
# password1=""
# password2=""
# password3=""
# for r_pass in range(1, nr_letters+1):
#     password1= password1+ random.choice(letters)

# for r_pass in range(1, nr_symbols+1):
#     password2= password2+ random.choice(symbols)

# for r_pass in range(1, nr_numbers+1):
#     password3= password3+ random.choice(numbers)
# final_pass = password1+password2+password3
# stringed_final_pass= list(final_pass)
# stringed_final_pass_random = random.shuffle(stringed_final_pass)
# joined_final_password = ' '.join(stringed_final_pass_random)
# print(joined_final_password)
# # print(random.shuffle(final_pass))

# # str_var = list("shuffle_this_string")
# # random.shuffle(str_var)
# # print ''.join(str_var)
# print(stringed_final_pass) 



#******************* Tough password generator********************** # 

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = [ ]

for r_pass in range(1, nr_letters+1):
    password_list= password_list+ random.choice(letters)

for r_pass in range(1, nr_symbols+1):
    password_list= password_list+ random.choice(symbols)

for r_pass in range(1, nr_numbers+1):
    password_list= password_list+ random.choice(numbers)
print(password_list)
