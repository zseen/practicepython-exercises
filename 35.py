import json
from collections import Counter

with open("info.json", "r") as f:
    birthdaysDict = json.load(f)

months = []
for key, value in birthdaysDict.items():
    splitValue = value.split(" ")
    month = splitValue[len(splitValue)-1]
    months.append(month)

countMonths = Counter(months)
print(countMonths)

