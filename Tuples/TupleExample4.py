#TupleExample4.py --------

tuple1 = (1,2,3)
print("Tuple1 = ", tuple1)

# For Repetition
tuple2 = ()
tuple2 = tuple1*2
print("tuple1*2 = ",tuple2)

# For Concatenation use '+'
tuple3 = ()
tuple3 = tuple1+tuple2
print("tuple1+tuple2 = ",tuple3)

# For Membership use 'in'
print("is 2 in tuple1 =",(2 in tuple1))
print("is 4 in tuple1 = ",(4 in tuple1))

# for length user 'len()'
print("length of tuple1 = ",len(tuple1))
print("length of tuple2 = ",len(tuple2))
print("length of tuple3 = ",len(tuple3))