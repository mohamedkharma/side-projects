print('''\nQ3: Python3 function to create a 2D list and another function to project it. \n ''')

def twoD(I,J):
    mylist =[] 
    print('\nA 2D list that contain the given values for I:\n')
    for i in range (0,len(I),2): 
            mylist.append(I[i:i+2]) 
    #print the list
    for row in mylist:
        for col in row:
            print (col, end = ' ')
        print('')
    #send to a new function
    projection(J,mylist)

def projection(J,mylist):
    try:   
        for i in J:
            print(f'At index {i}, the coordinates are: ',mylist[i-1])
    except:
        print(f'At index {i}, there is no coordinates because its out of range!\n')

I= [1, 2.09, 3, 4, 5, 6, 'a', 8, 9, 10.14, 11, 'b']
J= {1, 2, 7}   
twoD(I,J)
