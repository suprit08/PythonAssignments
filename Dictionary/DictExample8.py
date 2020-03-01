#DictExample8.py

student = {"name":"sumit","college":"stanford","grade":"A"}

#this will prints whole key and values pairs using items()

for x in student.items():
    print(x)


print("-----------------------------------------------------")


#you can also store key and value in two differnet variable like

for x,y in student.items():
    print(x,"-",y)

