x=str(input("Write some words please:"))

def reverseWords(x):
    result = x.split()
    reverse = result[::-1]
    reverse = ' '.join(reverse)
    return reverse

y=reverseWords(x)
print (y)
