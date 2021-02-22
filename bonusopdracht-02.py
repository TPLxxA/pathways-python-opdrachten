# Oplossing 1
ans = int(input("What is 15 + 25? "))
if ans == 40:
    print("That is correct")
else:
    print("Wrong :(")

# Oplossing 2 (advanced)
answergiven = False
while answergiven == False:
    ans = input("What is 15 + 25? ")
    try:
        ans = int(ans)
        answergiven = True
        if ans == 40:
            print("That is correct")
        else:
            print("Wrong :(")
    except:
        print("Please input a valid integer")
        break