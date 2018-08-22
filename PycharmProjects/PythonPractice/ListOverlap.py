a = [int(x) for x in input("Please enter series of numbers: ").split()]
b = [int(y) for y in input("Please enter second series of numbers: ").split()]

c = []

for num in a:
    if num in b:
        c.append(num)
    else:
        pass

print(c)