import random


def myStrip(x):
    return x.strip()


class RandomSOWPODSGenerator(object):

    def __init__(self):
        self.lines = None

    def generate(self):
        if self.lines is None:
            raise RuntimeError("generate called before initLines")
        randomIndex = random.randint(0, (len(self.lines) - 1))
        return self.lines[randomIndex]

    def initLines(self):
        self.lines = RandomSOWPODSGenerator.__createLines()

    @staticmethod
    def __createLines():
        with open('SOWPODS.txt', 'r') as f:
            lines = f.readlines()
            strippedLines = list(map(myStrip, lines))

        return strippedLines


def main():
    p = RandomSOWPODSGenerator()
    p.initLines()
    for _ in range(0, 100):
        print(p.generate())


if __name__ == "__main__":
    main()

