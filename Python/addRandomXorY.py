print('''\nQ2: A function that randomly adds either `X' or `Y' to the end of each
line.And another function to show the number of the lines finishing with XX and YY and the ratio of the lines
finishing with `XX' and `YY' / all n-lines.\n''')

import random # Importing module random for generating random numbers

letters = ['X','Y']
countlines = 0

file = open('addxory.txt','w') # Opening the file in write mode
for i in range(1000): # Repeat 1000 times
 
    r = random.randint(0,1) # Generating either 0 or 1
    XorY = letters[r]  # Generating X or Y based on the index generated
    file.writelines( f"This line ends with a random: {XorY}\n") # Write to the file
file.close()

def addXorY(filename):
    letters = ['X','Y']
    file = open(filename,'r') # Open the given text file in read mode
    content = file.readlines()  # Reading all the 1000 lines and storing them
    file.close()

    file = open(filename,'w') # Opening the same file again in write mode
    for line in content: #For each line
        line = line.replace("\n", "")# Remove the newline character
        Idx = random.randint(0, 1)  # Generate either 0 or 1

        # Add either X or Y from list letters based on the random index generated
        line = line + letters[Idx] + "\n"
        # Write the line to the file
        file.write(line)
    file.close()

def show_and_count(filename):
    doubleX = doubleY = 0
    file = open(filename,'r') # Opening the given file
    content  = file.readlines() # Reading all the lines from the file
    # For each individual line read, remove the newline
    for line in content:
        line = line.replace("\n","")
        if (line[-2:] == "XX"):
            doubleX += 1
        elif (line[-2:] == "YY") :
            doubleY += 1

    # Displaying
    print(f"\nNumber of lines that ends with double XX: {doubleX}")
    print(f"Number of lines that ends with double YY: {doubleY}")

    # Calculating the ratio
    ratio = (doubleX + doubleY) / 1000
    print(f"\nRatio of lines ending with XX and YY to total lines: {ratio}")

addXorY("addxory.txt")
show_and_count("addxory.txt")
