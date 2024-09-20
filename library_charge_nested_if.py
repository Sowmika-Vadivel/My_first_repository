days =int(input("enter the no of days :"))
if days <=10:
    if days <=5:
        sum= days*5
        print(f"your charge is {sum}")
    else : 
        sum=days*4
        print(f"your charge is {sum}")
else:
    if days <=5:
        sum= days*3
        print(f"your charge is {sum}")
    else:
        sum= days*2
        print(f"your charge is {sum}")
()