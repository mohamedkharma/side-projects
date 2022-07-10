
print("\nThis program is going to check whether the 3 points on the coordinate plane creates a triangle or not.")
def get_coordinates():
        x = float(input("Enter the coordinate of x: "))
        y = float(input("Enter the coordinate of x: "))
        return x,y

# Function to check that create a triangle 
def is_triangle(x1, y1, x2, y2, x3, y3): 
        
        #find area of triangle
        area = ((x1 * (y2 - y3) +
                x2 * (y3 - y1) +
                x3 * (y1 - y2)) / 2) 

        if area < 0:    # if area is negative
        	area *= -1  # returns positive area

        if area != 0: # if area doesn't equal zero, then its a triangle
           	print(f'The coordinates does creates a triangle.')
        else:
            print(f'The coordinates does NOT create a triangle.')
        return area

flag = True
while (flag):
	try:
		print("First point (x1,y1)")
		x1,y1 = get_coordinates()
		print("\nSecond point (x2,y2)")
		x2,y2 = get_coordinates()
		print("\nThird point (x3,y3)")
		x3,y3 = get_coordinates()
		
		area = is_triangle(x1,y1,x2,y2,x3,y3)

		print("\nWould you like to try again?")
		choice = str(input("Enter 'Yes' to try again or 'No' to quit: ")).upper() # checks user choice to continue
		while not (choice[0] == 'Y' or choice[0] == 'N'):                                                   
			choice = str(input("Please try entering 'Yes' or 'No' as an input: ")).upper()
		# Checks if user says No, so we exit the while loop
		if choice[0] == 'N':
			flag = False 
		else:
			True     # Ternary operator

	except ValueError: # checks if the user entered any invalid inputs 
		print("Your input is not a valid. Please enter an integer only!")
