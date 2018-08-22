x  = int(input("Please enter a number: "))

arr = range (1,x+1)

divisorList = []

for y in arr:
    if x % y == 0:
        divisorList.append(y)
    else:
        pass

print (divisorList)
