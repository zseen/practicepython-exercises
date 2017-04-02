import random
from random import randint


a = [random.randint(1,10) for item in range(random.randint(1,10))]
b = [random.randint(1,10) for item in range(random.randint(1,10))]
c=[item for item in a if item in b]
same=set(c)
print(a)
print(b)
print (same)