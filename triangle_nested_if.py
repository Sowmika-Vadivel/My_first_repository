side1=int(input("enter number 1:"))
side2=int(input("enter number 2:"))
side3=int(input("enter number 3:"))
if side1==side2:
    if  side1==side3:
        print("triangle is equilateral")
    else : 
        print("triangle is isoceles")
else:
    if side2==side3 :
        print("triangle is isoceles")  
    else:
        print("triangle is scalene")

