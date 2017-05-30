import random

class Hangman(object):


    def __init__(self):
        self.randomWord = None
        self.underscoreList = []


    def getAWord(self):
        textForWord = []
        with open('SOWPODS.txt', 'r') as f:
            line = f.readline().strip()
            textForWord.append(line)
            while line:
                line = f.readline().strip
                textForWord.append(line)

        randomIndex = random.randint(0, (len(textForWord)-1))
        self.randomWord = textForWord[randomIndex]

    def getAnInput(self):
        askForLetter = input(str("Give me a letter please!:"))


    def letterInWord(self):
        self.randomWord
        self.charRandomWord = self.randomWord.split(" ")

        for item in self.charRandomWord:
            self.printUnderscore()
            if self.getAnInput() not in self.charRandomWord:
                return False


        index = 0
        for _ in range(0, len(self.charRandomWord)):
            if self.charRandomWord[index] == self.getAnInput():
                del.self.underscoreList[index]
                self.underscoreList.insert(index, self.getAnInput())

    def printUnderscore(self):
        for i in range(0, len(self.charRandomWord)):
            self.underscoreList.append(_)
        return self.underscoreList

    def playHangman(self):
        while
        self.getAWord()
        self.getAnInput()
        self.letterInWord()



def main():
    h = Hangman()
    h.playHangman()


