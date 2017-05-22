def tellMax(numItems):
    while True:
        try:
            userInput=input("Give me %s numbers in this format: x,y,z!:" % numItems)
            userInputList=userInput.split(",")
            if len(userInputList)==numItems:
                userInputList.sort()
                return int(userInputList[-1])
                break
            else:
                print("I would like to get %s numbers please" % numItems)
        except ValueError as ve:
            print("Are you sure that you wrote numbers like this: x,y,z?")


def main():
    resultMax = tellMax(5)
    print(resultMax)

if __name__=="__main__":
    main()





