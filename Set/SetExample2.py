#SetExample2.py

#Adding elements to the set

month = set(["jan","feb","mar","apr","may","jun"])
print("\nPrinting the original set : ")
print(month)

#adding single element by using 'add()'
print("\nAdding some elements to the Set:")
month.add("jul")
month.add("aug")
print("\nModified Set : ",month)

#adding more elements by using 'update()'
print("\nAdding multiple elements :")
month.update(["oct","nov","dec"])
print("\nmodified set :")
print(month)

