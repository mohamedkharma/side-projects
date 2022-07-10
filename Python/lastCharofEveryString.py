print("This program will trims one character from end of any string and print until k characters")
def word_fadding(word, k):
    print(word)    #print the original string.

    length=len(word) #number of characters in the word
    n=length-k  #(number of characters in the word) - k indenx
    for x in range(n):
        word=word[:-1]  # going in reverse
        print(word)   #print new string after the remove of last character in each iteration.
# string and store the word.        
word = input("Enter any string: ")
# k indicates how many characters are left
k = int(input("Enter an intger to indicate at what index you wolud like the program to stop: "))

word_fadding(word,k)
