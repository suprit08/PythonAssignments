#SetExample3.py

#removing elements from set

months = {"jan","feb","mar","apr","may","jun","jul","oct"}
print("Set of months = ",months)

print("---------------------------------------------------")

#remove using 'discard()'
months.discard("jan")
print("modified set with discard('jan'):")
print(months)

print("---------------------------------------------------")

#remove using 'remove()'
months.remove("feb")
print("modified set with remove('feb'):")
print(months)

print("---------------------------------------------------")

#remove using 'pop()' to remove last item
months.pop()
print("modified set with pop():")
print(months)

print("---------------------------------------------------")

#remove all using clear()
months.clear()
print("modified set with clear():")
print(months)

print("---------------------------------------------------")