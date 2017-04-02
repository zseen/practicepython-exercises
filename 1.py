name=input("What is your name?:")
age=int(input("How old are you?:"))
year=(2017-age+100)
if age<0:
    print ("You cannot be younger than 0")
else:
    print(name + " will be 100 years old in the year " + str(year))