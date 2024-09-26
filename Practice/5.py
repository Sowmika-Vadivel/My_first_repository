# Question - 5 
# Write a Program to find the sum, difference, product and division, Between 2 integer numbers.
num_1=int(input("enter the number_1 :"))
num_2=int(input("enter the number_2 :"))
print(f"The sum of {num_1} & {num_2} is {num_1+num_2}")
print(f"The difference of {num_1} & {num_2} is {num_1-num_2}")
if num_1 != 0 and num_2 !=0 :
    print(f"The product of {num_1} & {num_2} is {num_1*num_2}")
    print(f"The division of {num_1} & {num_2} is {num_1/num_2}")
else:
     print(f"The product of {num_1} & {num_2} is 0")
     print(f"The division of {num_1} & {num_2} is invalid")