# a = [5, 10, 15, 20, 25]
# b=[a.pop(0), a.pop()]
# print (b)
#
#
#
#
# print(a)
#
# a = [input("Type some numbers please:")]
# for y in range(len(a) - 1):
#    a.append(y)
# print (a)

def firstandlast(a):
    b=[a.pop(0), a.pop()]
    return b

text = input("Type some numbers please:")
l = text.split()
l = list(map(int, l))

x=firstandlast(l)
print(x)

