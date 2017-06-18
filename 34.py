import json


class ScientistBirthdays(object):

    def __init__(self):
        with open("info.json", "r") as f:
            self.birthdaysDict = json.load(f)

    def addSomeone(self):
        ScientistBirthdays.name = input("Whose birthday would you like to add?:")
        if ScientistBirthdays.name in self.birthdaysDict:
            print("I already know it, it is on %s" % self.birthdaysDict[ScientistBirthdays.name])

        else:
            date = input("When is her/his birthday?:")
            self.birthdaysDict[ScientistBirthdays.name] = date
            print("I have added %s to my dictionary." % ScientistBirthdays.name)
            with open("info.json", "w") as f:
                json.dump(self.birthdaysDict, f)

    def whoseBirthdayPrint(self):
        ScientistBirthdays.whoseBirthday = input("Whose birthday would you like to see?:")
        if ScientistBirthdays.whoseBirthday in self.birthdaysDict:
            print("It is (on) %s." % self.birthdaysDict[ScientistBirthdays.whoseBirthday])
        else:
            ScientistBirthdays.askIfAdd = input("Sorry, I don't know his/her birthday. "
                                                "Would you like to add it? If yes, write'yes':")
            if ScientistBirthdays.askIfAdd == 'yes':
                ScientistBirthdays.addSomeone(self)

    @staticmethod
    def continueToAdd():
        ScientistBirthdays.answer = input("Would you like to continue? If yes, write 'yes', if not, write 'no':")
        if ScientistBirthdays.answer == 'yes':
            return True
        else:
            return False

    def optionsToDo(self):
        ScientistBirthdays.whatToDo = input("What would you like to do? Look up someone's birthday (type '1') "
                                            "or add someone's birthday(type '2') or exit (type '3')?:")
        if ScientistBirthdays.whatToDo == '1':
            self.whoseBirthdayPrint()
        elif ScientistBirthdays.whatToDo == '2':
            self.addSomeone()
            self.continueToAdd()
        elif ScientistBirthdays.whatToDo == '3':
            print("Bye, I hope you had fun!")
            raise SystemExit


def main():
    s = ScientistBirthdays()
    s.optionsToDo()

if __name__ == "__main__":
    main()


while True:
    try:
        main()
    except ValueError as ve:
        print("Ohh, a value error")
    except KeyError as ke:
        print("Ohh, a key error")











