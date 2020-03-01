#FileCopyExample5.py

SFile = input("Enter the name of Source file with extension:")

try:
    with open(SFile,'r') as rp:
        sfdata=rp.read()
        DFile = input ("Enter Destination file:")
        with open(DFile,'a') as wp:
            wp.write(sfdata)
            print('data copied successfully')

except FileNotFoundError:
    print("File doesn't exists")

else:
    print("Process completed......[OK]")


