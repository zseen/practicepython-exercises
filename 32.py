import random

DEBUG_TRACE = False


class Hangman(object):
    def __init__(self):
        self.randomWordLetters = None
        self.randomWordLettersHidden = None
        self.alreadyGuessed = None
        self.guessesLeft = 6
        self.bodyParts = []

    def __initialiseGame(self):
        self.alreadyGuessed = set()

        generatedRandomWord = Hangman.__generateRandomWord()
        self.randomWordLetters = list(generatedRandomWord)

        self.randomWordLettersHidden = []
        for i in range(0, len(self.randomWordLetters)):
            self.randomWordLettersHidden.append("_")

        self.__initialiseBodyParts()

        if DEBUG_TRACE:
            print(" ".join(self.randomWordLetters))

    def __initialiseBodyParts(self):
        self.bodyParts = [None] * 6
        self.bodyParts[0] = "O"  # head
        self.bodyParts[1] = "|"  # torso
        self.bodyParts[2] = "\\"  # leftArm
        self.bodyParts[3] = "/"  # rightArm
        self.bodyParts[4] = "/"  # leftLeg
        self.bodyParts[5] = "\\"  # rightLeg

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
            self.__takeGuessAway()
            self.__printHangmanFigure()
        else:
            self.__updateHiddenWord(currentGuessLetter)

        self.__printHiddenWord()

    def __takeGuessAway(self):
        self.guessesLeft -= 1
        self.bodyParts[self.guessesLeft] = " "

    def __updateHiddenWord(self, currentGuessLetter):
        self.alreadyGuessed.add(currentGuessLetter)
        for index in range(0, len(self.randomWordLetters)):
            if currentGuessLetter == self.randomWordLetters[index]:
                del self.randomWordLettersHidden[index]
                self.randomWordLettersHidden.insert(index, currentGuessLetter)

    def __printHangmanFigure(self):
        print(self.bodyParts[2] + self.bodyParts[0] + self.bodyParts[3] )
        print(" " + self.bodyParts[1])
        print(self.bodyParts[4] + " " + self.bodyParts[5])


    @staticmethod
    def __wouldLikeANewGame():
        answer = input("Would you like to start a new game? If yes, type 'yes', if no, 'no':")
        if answer == 'yes':
            return True
        else:
            return False

    def playHangman(self):
        self.__initialiseGame()
        self.__printHiddenWord()
        self.__printHangmanFigure()
        roundCounter = 0
        while True:
            if self.guessesLeft == 0:
                print("Ohh, game over")
            playerInputLetter = Hangman.__getAnInput()
            self.__processCurrentGuess(playerInputLetter)
            roundCounter += 1
            if self.randomWordLettersHidden == self.randomWordLetters:
                print("")
                print("Yeeee, you won in %s guesses!" % str(roundCounter))
                break
            if self.guessesLeft > 0:
                print("")
                print("You have %s wrong guesses left" % str(self.guessesLeft))

    def playRepeatedly(self):
        while True:
            self.playHangman()
            newGame = Hangman.__wouldLikeANewGame()
            if newGame is False:
                print("I hope you had fun!")
                break


def main():
    h = Hangman()
    h.playRepeatedly()


if __name__ == '__main__':
    main()
