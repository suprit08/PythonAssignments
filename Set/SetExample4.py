#SetExample4.py ------difference between discard() & remove()

#from both remove() gives error if value not found

nums = {1,2,3,4}

#remove using discard()
nums.discard(5)
print("After discard(5) : ",nums)

#reove using remove()

try:
    nums.remove(5)
    print("After remove(5) : ",nums)
except KeyError:
    print("KeyError : Value not found")