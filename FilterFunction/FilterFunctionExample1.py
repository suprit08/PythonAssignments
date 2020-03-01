#Special Function - filter()
#accept list and filter the positive and negative values from the values of list

def isPos(x):
    if x>0:
        return True

def isNeg(x):
    if x<0:
        return True

def isZero(x):
    if x==0:
        return True


print("Enter the list values :")

lst = [int(x) for x in input().split()]

print('='*40)

poslist = list(filter(isPos, lst))
print("Positive =",poslist)

print('-'*40)

neglist = list(filter(isNeg, lst))
print("Negative =",neglist)

print('-'*40)

zlist = list(filter(isZero, lst))
print("Zeros = ",zlist)

print('-'*40)
