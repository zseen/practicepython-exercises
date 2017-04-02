# a=[0,2,4,6,8,11]


#see if number is in list and returns true or false
# def inList():
#     if x in a:
#         return True
#     else:
#         return False
#
# print (inList())

#binary thing
 # NO!
 # def binarySearch():
#     if (len(a))%2==0:     #6 elemu lista
#        if a[((len(a))//2)-1]==x:  #2. index 3.elem, 4
#            return True
#        elif:
#            a[((len(a)) // 2) - 1] > x: NOOO!!!

def binarySearch(numbersList, x):
    if len(numbersList) == 1:
        return True if numbersList[0] == x else False

    middle = int(len(numbersList) / 2)
    if numbersList[middle] == x:
        return True
    elif numbersList[middle] > x:
        return binarySearch(numbersList[:middle:], x)
    else:
        return binarySearch(numbersList[middle::], x)


def main():
    while True:
        try:
            a = [1, 2, 3, 4, 5]
            x = int(input("Type a number please: "))
            r = binarySearch(a, x)
            print(r)
            break
        except ValueError:
            print ("Number please")


if __name__=="__main__":
    main()




