""""
The user enters the length of the password
Then PasswordGenerator(l) is called taking the length of the password
And using random.choices, 
it generates a password consisting of uppercase & lowercase letters, digits and special characters using string.printable
"""

import random
import string

def PasswordGenerator(l):
    password = ''.join(random.choices(string.printable, k=l))
    return(password)

print("Password Generator")
length = int(input("Enter the length of your password: "))
password = PasswordGenerator(length)
print("Your Password: ", password)