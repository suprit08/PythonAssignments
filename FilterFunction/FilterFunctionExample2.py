#Filter Fucntion Example 2

def isVow(x):
    if x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
        return True

def isCons(x):
    if x!='a' and x!='e' and x!='i' and x!='o' and x!='u':
        return True
 
print("Enter the letters:")
lst = [x for x in input().split()]
print('-'*40)
vowlist = list(filter(isVow, lst))
print("Vowels =",vowlist)
print('-'*40)
conslist = list(filter(isCons, lst))
print("Consonents =",conslist)
print('-'*40)
