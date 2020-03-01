#PickleExample1.py
#pickle.load() ------File Reading Module (binary file)

from pickle import load
import sys

SFile = input("Enter the Source File name:")


try:
    with open(SFile,'rb') as rp:
        try:
            SFData = load(rp)
            print("Data of ",SFile," is loaded")
        except EOFError:
            print("File read operation ended.")
            sys.exit()
except FileNotFoundError:
    print("File doesn't exists")

else:
    print("Process Completed...............[OK]")