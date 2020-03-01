#FileExample4.py
#Program to count the no.of lines, no.of words, no.of characters in a file.
#----------------------------------------------------------------------------------

SFile = input("Enter the name of Source File:")
nl = 0 #no.of lines
nw = 0 #no.of words
nc = 0 #no.of characters

try:
    with open(SFile,'r') as rp:
        for line in rp:
            nl = nl + 1
            words = line.split()
            nw = nw + len(words)
            nc = nc + len(line)

    print('-'*50)
    print("No.of Lines:",nl)
    print("No.of Words:",nw)
    print("No.of Characters:",nc)
    print('-'*50)

except FileNotFoundError:
    print("File Doesn't Exists")