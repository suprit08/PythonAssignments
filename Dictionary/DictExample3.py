#DictExample3.py

print("---------------------------------------------------")

student = {"name":"sumit","college":"stanford","grade":"1"}
print("Student information :\n")
print("Student Name : ",student['name'])
print("College : ",student['college'])
print("grade : ",student['grade'])

print("---------------------------------------------------")

print("Modify the inputs:")
student['name'] = input("Enter the name : ")
student['college'] = input("Enter the college : ")
student['grade'] = input("Enter grade : ")

print("---------------------------------------------------")

print("\nmodified information :\n")
print("Student Name : ",student['name'])
print("Student college : ", student['college'])
print("Student Grade : ",student['grade'])

print("---------------------------------------------------")
