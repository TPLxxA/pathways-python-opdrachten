# Oplossing 1
for i in range(1,11):
    print(" " * (10 - i) + "#" * i)

# Oplossing 2
space = " "
step = "#"
stairs = ""
for i in range(10):
    stairs += space * (10 - i + 1)
    stairs += step * (i + 1)
    print(stairs)
    stairs = ""