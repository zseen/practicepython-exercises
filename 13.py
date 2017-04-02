while True:
    try:
        y=int(input("How many fibonacci numbers would you like to see?"))


        fib = [0,1]
        def fibonacci(y):
            a, b = 0, 1
            for x in range(y-2):
                a,b=b,a+b
                fib.append(b)
            return fib
        break
    except ValueError:
        pass



x=fibonacci(y)
print (x)

#
# def fibonacci(y):
#     x=0
#     a = 0
#     b = 1
#
#
# z=fibonacci(y)
# print(z)

# 0 1 1 2 3 5 8 13 21 34 55 89
# a=0
# b=1

