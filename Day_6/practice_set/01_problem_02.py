# Write a program to find the greatest of four numbers entered by the user.
a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))
c=int(input("Enter number 3:"))
d=int(input("Enter number 4:"))

if a>=b and a>=c and a>=d:
    print("The Max number is ",a)

if b>=a and b>=c and b>=d:
    print("The Max number is ",b) 

if c>=b and c>=a and c>=d:
    print("The Max number is ",c)


if d>=b and d>=c and d>=a:
    print("The Max number is ",d)