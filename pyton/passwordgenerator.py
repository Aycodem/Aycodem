from itertools import count
import string
import random

##character that generate password from
characters=list(string.ascii_letters + string.digits + " !@.#$%^&*()")

def generate_random_password():
    ## length of password from user
    length =int(input("Enter password length: "))

    ##picking random character
    password=[]
    for i in range(length):
        password.append(random.choice(characters))

    ##shuffling the resultant password 
    print(",".join(password))
        


generate_random_password()