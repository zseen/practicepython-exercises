while True:
    try:
        x=int(input("Type a number please:"))
        break
    except ValueError:
        pass

# possible=[]
# y=0

# while y<x:
#     y=y+1
#     possible.append(y)
# print (possible)

for i in range(1,x+1):
    if x%i==0:
        print (i)

