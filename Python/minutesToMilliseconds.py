print("""Program to convert minutes to milliseconds
for example if the user input 3 as the number
of minutes, then the output 180000 milliseconds.
	""")
number_of_minutes = int(input("Enter the number of minutes you would like to convert: "))
milliseconds = number_of_minutes * 60000

print("In", number_of_minutes, "minutes, there is :", milliseconds, "milliseconds")
