a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for x in a:
#     if x<5:
#         print (x)
#
# b=[]
# for x in a:
#    if x <5:
#        b.append(x)
# print (b)

def divide(a, b):
    if b == 0:
        raise ValueError("Divisor is 0")

    if a > 1000:
        raise ValueError("a is too large")

    if b < -2:
        raise RuntimeError("fatal error")

    return a / b

try:
    number = divide(500, 0)
    print(number)
except ValueError as ve:
    print("Value error: " + str(ve))
except Exception as e:
    print("Exception: " + str(e))


# while True:
#     inputStr=(input("Type a number please:"))
#     try:
#         inputNum = float(inputStr)
#         break
#     except ValueError:
#         print("Invalid number, try again.")
#
# result=[]
#
# for elem in a:
#     if elem < inputNum:
#         result.append(elem)
# print (result)
