import _datetime

name = input("Give me your name: ")
print ("Your name is", name)

age = int (input("Please enter your age: "))
#print ("Your age is", age)

ageDiff = 100 - age

now = _datetime.datetime.now()
currentYear = now.year

futureYear = currentYear + ageDiff
print ("%s, you will turn 100 in the year %d." %(name,futureYear))