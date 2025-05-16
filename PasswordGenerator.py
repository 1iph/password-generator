import random
import string

# 1. Get the desired password length from the user
length = int(input("How long would you like this password to be?: "))
safe_symbol = "!"
# 2. Create a "master pool" of all possible characters
#    This combines all lowercase/uppercase letters, all digits, and all punctuation symbols
all_possible_chars = string.ascii_letters + string.digits + safe_symbol

# 3. Initialize an empty string to build the password
generated_password = ""

# 4. Loop 'length' number of times to build the password
for _ in range(length):
    # In each iteration, pick a random character from the 'all_possible_chars' pool
    random_chosen_char = random.choice(all_possible_chars)

    # Add the chosen character to the 'generated_password' string
    generated_password += random_chosen_char

# 5. After the loop finishes, print the complete generated password
print("Your generated password is:", generated_password)