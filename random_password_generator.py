# ask should contain length 
# --special characters , uppercase , numbers 
# get all avalable characters and randomly 
# select characters upto the length 
# atleast 1 of eact character type 
# ensure length is valid 

import random
import string

def generate_password():
    length = int(input("Enter the desired password length: ").strip())
    include_uppercase = input("Should it contain UpperCase characters (yes / no): ").lower().strip()
    include_special = input("Should it contain Special characters (yes / no): ").lower().strip()
    include_numbers =  input("Should it contain numbers (yes / no): ").lower().strip()
    
    if length < 4 :
        print("Password length should be atleast 4 characters")
        return
    
    lowerCase = string.ascii_lowercase
    upperCase = string.ascii_uppercase if include_uppercase == 'yes' else ""   #inline if statement or ternary statement 
    special = string.punctuation if include_special == 'yes' else ""  
    number = string.digits if include_numbers == 'yes' else "" 
    all_characters = lowerCase + upperCase + special + number
    
    required_characters = []
    if include_uppercase == 'yes':
        required_characters.append(random.choice(upperCase))
    if include_special == 'yes':
        required_characters.append(random.choice(special))
    if include_numbers == 'yes':
        required_characters.append(random.choice(number))

    remaining_length = length - len(required_characters)

    for _ in range(remaining_length):
        required_characters.append(random.choice(all_characters))
    
    random.shuffle(required_characters)
    password = "".join(required_characters)
    return password

password = generate_password()  
print(password)  