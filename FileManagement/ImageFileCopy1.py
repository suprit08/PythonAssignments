#ImageFileCopy1.py
#-----------------------------------------------------------------------

SFile = input("Enter the name of Image Source File:")
try:
    rp = open(SFile,'rb')  # here rb reprents reading of binary file.
    DFile = input("Enter the name of Destination image file:")
    wp = open(DFile,'ab')
    SFData = rp.read()
    wp.write(SFData)

except FileNotFoundError:
    print("File doesn't exists")

else:
    print(SFile," image copied to ",DFile," successfully!")
