word=str(input("Type a word please:"))
word=word.casefold()
new_word=word[::-1]



if word==new_word:
    print ("It is a palindrome")
else:
    print ("It is not a palindrome")