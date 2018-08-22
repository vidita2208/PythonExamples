a = [int(x) for x in input("Please enter a list of numbers: ").split()]

b = [y for y in a if (y%2== 0)]

print (b)