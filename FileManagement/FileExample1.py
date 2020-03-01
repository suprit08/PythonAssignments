#FileExample1.py

#open file in write mode.
fp = open("file1.dat",'w')

#Predifened Functions
print("------------------------------------------------------")
print("Name of File:",fp.name)
print("Mode of File:",fp.mode)
print("Is it readable?:",fp.readable())
print("Is it writable?:",fp.writable())
print("Is it closed:",fp.closed)
print("------------------------------------------------------")

#closing file
fp.close()
print("File Closed")

#Checking after close()
print("Is it closed:",fp.closed)