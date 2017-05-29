import random


class readAFile(object):

    @staticmethod
    def readSOWPODS():
        text = []
        with open('SOWPODS.txt', 'r') as f:
            line = f.readline().strip()
            text.append(line)
            while line:
                line = f.readline().strip()
                text.append(line)
        return text[random.randint(0, (len(text) - 1))]


def main():
    r = readAFile()
    print(r.readSOWPODS())


if __name__== "__main__":
    main()

