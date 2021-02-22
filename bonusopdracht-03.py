# import this module for both solutions
import random

# Oplossing 1
firstnum = random.randint(0, 1000)
secondnum = random.randint(0, 1000)
ans = input("What is " + str(firstnum) + " + " + str(secondnum) + "? ")
if ans == (firstnum + secondnum):
    print("That is correct")
else:
    print("Wrong :(")

# Oplossing 2 (advanced)
# This solution is left as a challenge to the reader