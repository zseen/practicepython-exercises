class Guesser(object):
    def __init__(self):
        self.possibilities=[]
        for i in range(0, 101):
            self.possibilities.append(i)
    
    def play(self):
        inputBegin = input("Think of a number please, when ready, write 'ready' and I start guessing!:")
        if inputBegin == "ready":
            counter = 0
            while True:
                counter += 1

                middle = len(self.possibilities) // 2
                numberGuessed = self.possibilities[middle]

                guessingResult = input(
                    "My guess is %s. If right, write 'right', if too low, write 'low', if too high, write 'high':" % str(
                        numberGuessed))
                if guessingResult == "right":
                    print("Hooray")
                    print("It took me %s guesses" % str(counter))
                    break
                elif guessingResult == "low":
                    del self.possibilities[0:middle]
                elif guessingResult == "high":
                    del self.possibilities[middle:]
        

def main():
    guesser = Guesser()
    guesser.play()

if __name__=="__main__":
    main()