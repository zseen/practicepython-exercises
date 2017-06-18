import json
from collections import Counter


def monthsCounter():
    with open("info.json", "r") as f:
        birthdaysDict = json.load(f)
    months = []
    for key, value in birthdaysDict.items():
        splitValue = value.split(" ")
        month = splitValue[len(splitValue)-1]
        months.append(month)
    return Counter(months)


def main():
    countTheMonths = monthsCounter()
    print(countTheMonths)

if __name__ == "__main__":
    main()


