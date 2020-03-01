#AssertExample1.py

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

def subs(a,b):
    assert a>b, "First number shouldn't be small"
    return a-b

cal = subs(num1,num2)
print(cal)