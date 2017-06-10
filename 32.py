import random

DEBUG_TRACE = False


class Hangman(object):
    def __init__(self):
        self.randomWordLetters = None
        self.randomWordLettersHidden = None
        self.alreadyGuessed = None
        self.guessesLeft = 6

    def __initialiseGame(self):
        self.alreadyGuessed = set()

        generatedRandomWord = Hangman.__generateRandomWord()
        self.randomWordLetters = list(generatedRandomWord)

        self.randomWordLettersHidden = []
        for i in range(0, len(self.randomWordLetters)):
            self.randomWordLettersHidden.append("_")

        if DEBUG_TRACE:
            print(" ".join(self.randomWordLetters))

    @staticmethod
    def __generateRandomWord():
        with open('SOWPODS.txt', 'r') as f:
            lines = f.readlines()
            wordList = [x.strip() for x in lines]
        randomIndex = random.randint(0, len(wordList) - 1)
        randomWord = wordList[randomIndex]
        return randomWord

    @staticmethod
    def __getAnInput():
        inputChar = input(str('Give me a letter please!:'))
        inputChar = inputChar.upper()
        return inputChar

    def __printHiddenWord(self):
        print(" ".join(self.randomWordLettersHidden))

    def __processCurrentGuess(self, currentGuessLetter):
        if currentGuessLetter in self.alreadyGuessed:
            print("Ohh, you have already guessed this letter")
        elif currentGuessLetter not in self.randomWordLetters:
            print("Ohh, your letter is not in the word")
            self.guessesLeft -= 1
        else:
            self.__updateHiddenWord(currentGuessLetter)
            self.__printHiddenWord()

    def __updateHiddenWord(self, currentGuessLetter):
        self.alreadyGuessed.add(currentGuessLetter)
        for index in range(0, len(self.randomWordLetters)):
            if currentGuessLetter == self.randomWordLetters[index]:
                del self.randomWordLettersHidden[index]
                self.randomWordLettersHidden.insert(index, currentGuessLetter)

    def playHangman(self):
        self.__initialiseGame()
        self.__printHiddenWord()
        roundCounter = 0
        while self.guessesLeft <= 6:
            if self.guessesLeft == 0:
                print("Ohh, game over")
                break
            playerInputLetter = Hangman.__getAnInput()
            self.__processCurrentGuess(playerInputLetter)
            self.__updateHiddenWord(playerInputLetter)
            roundCounter += 1
            if self.randomWordLettersHidden == self.randomWordLetters:
                print("Yeeee, you won in %s guesses!" % str(roundCounter))
                break
            if self.guessesLeft > 0:
                print("You have %s guesses left" % str(self.guessesLeft))


def main():
    h = Hangman()
    h.playHangman()


if __name__ == '__main__':
    main()
