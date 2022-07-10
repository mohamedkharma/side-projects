
print("""\nThis program will find all prime numbers between two inclusive integer numbers.
Prime numbers will be displayed to the screen and saved in 'primes.txt' file.""")

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

file = open('primes.txt', 'w')  # 'w' allows us to overwrite the numbers inside prime.txt file
print(f"Prime numbers between {num1} and {num2} are:")
for i in range(num1, num2 + 1):	# Go left by one becasue num2 is inclusive
   
   if i > 1:	# all prime numbers starts after 1
       for j in range(2, i): 	 # i is exclusive
           if (i % j) == 0:
               break
       else:
           print(i)
           file.write(str(i) + '\n') 	# write i to prime.txt file
file.close()              
