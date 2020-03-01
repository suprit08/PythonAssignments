#DictExample4.py  ------Deleting elements using del keywords

print("--------------------------------------------------")

student = {"name":"sumit","college":"stanford","grade":"A"}

print(student)

print("--------------------------------------------------")

print("Deleting some elements using del keyword : ")
del student['grade']

print("--------------------------------------------------")

print("Modified Information : ")

print(student)

print("--------------------------------------------------")

print("Deleting student : ")

del student

# It will show the NameError because student is eliminated.
print("student = ",student)

print("--------------------------------------------------")