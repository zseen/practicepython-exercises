def divisors(x):
    divisorList=[]
    for i in range(1,x+1):
        if x%i==0:
            divisorList.append(i)
    return divisorList

def main():
    while True:
        try:
            x = int(input("Type a number please:"))
            break
        except ValueError:
            pass
    y=divisors(x)
    print (y)

if __name__=="__main__":
    main()


