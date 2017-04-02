a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#result = []
#for element in a:
#    if element in b:
#        result.append(element)

#print (result)

same_values = set(a) & set(b)
print (same_values)
