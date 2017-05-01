def readFileAsList(filename):
    with open(filename) as file:
        numberslist = file.readlines()
    numberslist = [int(x.strip()) for x in numberslist]

    return numberslist

def sortedOverlap(list1, list2):
    return sorted(list(set(list1).intersection(list2)))

def main():
    happynumbersList = readFileAsList("happynumbers.txt")
    primenumbersList = readFileAsList("primenumbers.txt")
    overlapList = sortedOverlap(happynumbersList, primenumbersList)

    print(overlapList)

if __name__ == "__main__":
    main()