#ListExample2.py ----using some built-in methods in python

print("-"*70)

#Empty list
lst = []
print("Empty List  \nlst =",lst)

print("---------------------------------------------------------")

#Adding elements to list
lst.append(1)
lst.append("suprit")
lst.append(20.19)
print("After adding an element  \nlst=",lst)

print("---------------------------------------------------------")

#Clearing List
lst.clear()
print("After clearing \nlst=",lst)

print("---------------------------------------------------------")

#Making copy of lst
lst1 = [1,"Suprit",20.19]
print("First List lst1: ",lst1)

lst2 = lst1.copy()

print("lst2 after copying lst1 to it:",lst2)

print("---------------------------------------------------------")

#adding multiple elements to the list with extend()
alist = ['sumit',20.23,True]
print("New list to add (list) = ",alist)

atuple = (1,"sherif")
print("New tuple to add (atuple) = ",atuple)

aset = {"shruti",100}
print("New set to add (aset) =",aset)

lst2.extend(alist)
print("After adding new list to existing :",lst2)

lst2.extend(atuple)
print("After adding new tuple to existing list:",lst2)

lst2.extend(aset)
print("After adding new set to existing list",lst2)

print("---------------------------------------------------------")

#Counting elements occurences in a list
print("Adding element again 'Suprit'")
lst1.append("Suprit")
print("Count of 'Suprit' in lst1 = ",lst1.count("Suprit"))

print("---------------------------------------------------------")

