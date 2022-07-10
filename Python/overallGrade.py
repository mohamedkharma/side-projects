print("""Program to calculate the overall grade using 
the midterm and the final grades as inputs""")

midterm = int(input("Enter Midterm grade: "))
final = int(input("Enter Final grade: "))
grade = midterm * .4 + final * .6

print("Overall grade is:", grade)
