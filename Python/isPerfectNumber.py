print('''Program to check a perfect number is a positive integer 
that is equal to the sum of its proper positive divisors\n''')
# This function is to find perfect num
def isPerfectNumber(num):
    totalNums = 0
    for i in range(1,num): # begin dividing with 1 because 0 will result in error.
        if num % i == 0:
            totalNums += i
    return totalNums == num    # returns true if totalNums == num

    
flag = True
while flag:     #keep running as long as its true 
        try:
            num = int(input("Enter a number to check whether its a perfect or not: "))
            if isPerfectNumber(num) == True:
                    print(f"{num} is a perfect number!")
            else:
                    print(f"{num} is not a perfect number!")

            print("\nWould you like to try different number?")
            select = str(input("Enter 'Yes' to try again or 'No' to quit: ")).upper() # checks user selected choice to continue
            while not(select[0] == 'Y' or select[0] == 'N'):
                    select = str(input("Try entering either 'Yes' to try again or 'No' to quit: ")).upper() # checks user selected choice to continue
            if (select[0] == 'N'):
                    flag = False
            else:
                    flag = True
        except ValueError:
                print(f"{num} is not an integer. Try entering an integer")

