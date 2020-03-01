#Area of Circle ---Pattern1
while True:
    def circleArea(r):
        area=3.14*r*r
        print("Area of cirlce: ",area)

    rad=int(input("Enter the Radius of Circle:"))
    circleArea(rad)
    print("-"*40)
else:
    print("Enter valid input")
    
