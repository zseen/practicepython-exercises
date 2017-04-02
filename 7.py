a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b=[]
for even in a:
    if even%2==0:
        b.append(even)
print (b)

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b=[number for number in a if number % 2 == 0]
print(b)