#ListExample1.py ------Simple List

print("-"*50)
lst1 = ["Eno","Ename","Designation","Salary"]
lst2 = [1,'suprit','software engineer',10.00]
print(lst2)
print("-"*50)
#using len method
print("List2 item counts:",lst1.__len__())
print("List2 items count:",lst2.__len__())
#using min() and max()
print("Maximum element of list1:",max(lst1))
print("Minimum element of list1:",min(lst1))
