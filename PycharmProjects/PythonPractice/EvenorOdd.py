num = int(input("Please enter a number: "))

# A little modification here.
if (num == 0):
    print("The entered number is zero.")

elif (num % 2 == 0):
    print("The number is an even number.")
    #Modification:1.
    if (num % 4 ==0):
        print("The number is a multiple of 4.")
    else:
        pass

else:
    print("The number is an odd number.")