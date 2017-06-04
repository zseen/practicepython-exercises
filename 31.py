import random


class Hangman(object):
    def __init__(self):
        self.randomWord = None
        self.charRandomWord = []
        self.askForLetter = None
        self.underscoreList = []
        self.strCharRandomWord = None
        self.strPrintUnderscore = None
        self.strUnderscoreList = None
        self.alreadyGuessed = set()

    def getAWord(self):
        with open('SOWPODS.txt', 'r') as f:
            line = f.readlines()
            textForWord = [x.strip() for x in line]
        randomIndex = random.randint(0, len(textForWord) - 1)
        self.randomWord = textForWord[randomIndex]
        print(self.randomWord)

        self.charRandomWord = list(self.randomWord)
        self.strCharRandomWord = ",".join(self.charRandomWord)
        print(self.strCharRandomWord)

    def getAnInput(self):
        self.askForLetter = input(str('Give me a letter please!:'))

    def printUnderscores(self):
        for i in range(0, len(self.charRandomWord)):
            self.underscoreList.append("_")
        self.strPrintUnderscore = " ".join(self.underscoreList)
        print(self.strPrintUnderscore)

    def underscoreOrLetter(self):
        if self.askForLetter in self.alreadyGuessed:
            print("Ohh, you have already guessed this letter")
        elif self.askForLetter not in self.charRandomWord:
            print("Ohh, your letter is not in the word")

        else:
            self.alreadyGuessed.add(self.askForLetter)
            for index in range(0, len(self.charRandomWord)):
                if self.askForLetter == self.charRandomWord[index]:
                    del self.underscoreList[index]
                    self.underscoreList.insert(index, self.askForLetter)
                    self.strUnderscoreList = " ".join(self.underscoreList)

            print(self.strUnderscoreList)
    # def letterInWord(self):
    #     for item in range(0, len(self.randomWord)):
    #         if self.askForLetter == self.charRandomWord[item]:
    #             print(self.askForLetter, end='')
    #         else:
    #             print("_ ", end='')

    def playHangman(self):
        self.getAWord()
        # x = self.printUnderscore()
        self.printUnderscores()
        while self.underscoreList != self.charRandomWord:
            self.getAnInput()
            # self.letterInWord()
            self.underscoreOrLetter()
            if self.underscoreList == self.charRandomWord:
                print("Yeeee, you won!")
                break



def main():
    h = Hangman()
    h.playHangman()


if __name__ == '__main__':
    main()
