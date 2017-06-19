import json
from collections import Counter


def countTheMonths():
    with open("info.json", "r") as f:
        birthdaysDict = json.load(f)
    months = []
    for key, value in birthdaysDict.items():
        splitValue = value.split(" ")
        month = splitValue[len(splitValue)-1]
        months.append(month)
    return Counter(months)


def main():
    monthsCounter = countTheMonths()
    print(monthsCounter)

if __name__ == "__main__":
    main()


