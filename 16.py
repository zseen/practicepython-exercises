import random
from random import randint
from string import punctuation

numbers =[1, 2, 3, 4, 5, 6, 7, 8, 9]
lowercase =['a','b','c','d','e','f','g','h','i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
special = ['*', '?', '!', '@']

def generate_password():
    password = []

    numIters = random.randint(3, 5)
    for _ in range(0, numIters):
        password.append(random.choice(numbers))
        password.append(random.choice(lowercase))
        password.append(random.choice(uppercase))
        password.append(random.choice(special))

    password = ''.join(str(e) for e in password)
    return password

result = generate_password()
print("Your password is: %s " %str(result) )
