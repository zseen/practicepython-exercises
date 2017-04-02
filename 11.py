# def primenumber(x):
#     divisor = []
#     y = 0
#     while y < x:
#         y = y + 1
#         if x % y == 0:
#             divisor.append(y)
#     if len(divisor) == 2:
#         print("It is a prime number")
#     else:
#         print("It is not prime")
#
# while True:
#     try:
#         x = int(input("Type a number please:"))
#         primenumber(x)
#         break
#     except ValueError:
#         pass

#-----------------------------------------------------------------------------------------------
x = int(input("Type a numberrrrr please:"))
def primenumber(x):
    if x == 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False

    return True

isPrime = primenumber(x)
if isPrime:
    print ("It is prime")
else:
    print ("It is not prime")

