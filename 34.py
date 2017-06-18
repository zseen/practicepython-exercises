import json


class ScientistBirthdays(object):

    def __init__(self):
        self.birthdaysDict = None

    def loadDict(self):
        with open("info.json", "r") as f:
            self.birthdaysDict = json.load(f)

    def saveDict(self):
        with open("info.json", "w") as f:
            json.dump(self.birthdaysDict, f)

    def addSomeone(self):
        self.loadDict()

        name = input("Whose birthday would you like to add?:")
        if name in self.birthdaysDict:
            print("I already know it, it is (on) " + self.birthdaysDict[name])
        else:
            date = input("When is her/his birthday?:")
            self.birthdaysDict[name] = date
            print("I have added " + name + " to my dictionary.")
            self.saveDict()

    def whoseBirthdayPrint(self):
        self.loadDict()

        whoseBirthday = input("Whose birthday would you like to see?:")
        if whoseBirthday in self.birthdaysDict:
            print("It is (on) " + self.birthdaysDict[whoseBirthday])
        else:
            askIfAdd = input("Sorry, I don't know his/her birthday. "
                             "Would you like to add it? If yes, write 'yes':")
            if askIfAdd == 'yes':
                self.addSomeone()

    def optionsToDo(self):
        whatToDo = input("What would you like to do? Look up someone's birthday (type '1') "
                         "or add someone's birthday(type '2') or exit (type '3')?:")
        if whatToDo == '1':
            self.whoseBirthdayPrint()
        elif whatToDo == '2':
            self.addSomeone()
        elif whatToDo == '3':
            print("Bye, I hope you had fun!")
            raise SystemExit


def main():
    s = ScientistBirthdays()
    while True:
        try:
            s.optionsToDo()
        except ValueError as ve:
            print("Ohh, a value error: " + ve)
        except KeyError as ke:
            print("Ohh, a key error: " + ke)

if __name__ == "__main__":
    main()
