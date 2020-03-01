#FileCopyExample1
#------------------------------------------------------------------------------

SFile = input("Enter the Source File name with Extension:")

try:
    rp = open(SFile,'r')
    DFile = input("Enter the name of destination file with extension:")
    wp = open(DFile,'a')
    sfdata = rp.read()
    wp.write("\n")
    wp.write(sfdata)

except FileNotFoundError:
    print("File name doesn't exist")

else:
    print(SFile, " copied to ",DFile)