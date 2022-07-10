print('''Q1: Python3 function to compare each line of two files, character by character, and
if there is a match of the characters, create a variable representing the similarity between
the lines of each file.\n ''')
def compare_files(filename1,filename2):
    f1 = open(filename1,"r")
    f2 = open(filename2,"r")
    f1.read()
    f2.read()
    temp1 = f1.tell()
    temp2 = f2.tell()
    f1.seek(0)
    f2.seek(0)
    similarity = ''
    while ((f1.tell() != temp1) or (f2.tell() != temp2)):
        line1 = f1.readline()
        line2 = f2.readline()
        line1_size = len(line1)
        line2_size = len(line2)
        if len(line1) < line2_size:
            for i in range(0,line1_size):
                if line1[i] == line2[i]:
                    similarity += line1[i]
        else:
            for i in range(0,line2_size):
                if line1[i] == line2[i]:
                    similarity += line2[i]
    f1.close()
    f2.close()
    similarity = similarity.split()
    similarity = ''.join(similarity)
    print(f"The similarity between the two files is: {similarity}")

compare_files('A.txt','B.txt')
