a = [1, 1, 2, 3, 5, 8, 13, 13, 21, 34, 55, 55, 89]
# a=set(a)
# a=list(a)
# print(a)

def filterDuplicatesWithSet(a):
    a=set(a)
    a=list(a)
    return list(a)

x=filterDuplicatesWithSet(a)
print(x)

def filterDuplicatesWithList(a):
    b=[]
    for item in a:
        if item not in b:
            b.append(item)
    return b

y=filterDuplicatesWithList(a)
print(y)