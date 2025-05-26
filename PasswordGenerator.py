import random
import string

length = int(input("How long would you like this password to be?: "))
how_many = int(input("How many passwords would you like to generate?: "))
safe_symbol = "!"

for _ in range(how_many):
 all_possible_chars = string.ascii_letters + string.digits + safe_symbol


 generated_password = ""


 for _ in range(length):
    
    random_chosen_char = random.choice(all_possible_chars)

    
    generated_password += random_chosen_char


 print("Your generated password is:", generated_password)