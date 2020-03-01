#TupleExample3.py ------Tuple doesn't support deletion

#values of tuples are unchangable or undeletable

tuple1 = (1,2,3,4,5,6,7,8)

print(tuple1)

del tuple1[0]  #deleting element at index of 0th

print(tuple1)

del tuple1[4:5]  #deleting tuple elements from 4:5

print(tuple1)

del tuple1   # deleting the tuple1

print(tuple1)

