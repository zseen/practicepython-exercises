import random


class ReadAFile(object):

    @staticmethod
    def readSOWPODS():
        with open('SOWPODS.txt', 'r') as f:
            lines = f.readlines()

        randomIndex = random.randint(0, (len(lines) - 1))
        return lines[randomIndex]


def main():
    print(ReadAFile.readSOWPODS())


if __name__ == "__main__":
    main()

