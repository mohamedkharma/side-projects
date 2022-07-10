print('''\nQ5: to randomly shuffle the elements of 2D list 
and write it back to the file with that particular order.\n. ''')
import random
def shuffle2DList(filename):
	mainlist = [] 	# A list to store content of file
	file = open(filename,'r')	# open file in read mode
	F = file.read().splitlines()
	index = 0	#to count the elements
	for i in range(0,3):	# reading every line 
		l = []
		for j in range(0,4):
			l.append(int(F[index]))	  #insert each line in List
			index += 1
		mainlist.append(l)
	file.close()
	print("File content BEFORE shuffling the numbers: \n")
	for rows in mainlist:
		for columns in rows:
			print(columns, end= ' ')
		print('')

	print("\nFile content AFTER shuffling the numbers: \n")
	random.shuffle(mainlist)	# randomly shuffle the list
	for rows in mainlist:
		for columns in rows:
			print(columns, end= ' ')
		print('')

	file = open(filename,'w')	# open file in read mode
	for rows in range(0,3):	# reading every line 
		for columns in range(0,4):
			file.write(str(mainlist[rows][columns])+'\n')
	file.close()
  
shuffle2DList('q5.txt')
