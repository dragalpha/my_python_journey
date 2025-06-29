# Write a program to find the greatest of four numbers entered by the user.

a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))
c=int(input("Enter number 3:"))
d=int(input("Enter number 4:"))

if(a>b):
    if(a>c):
        if(a>d):
            print("The highest number along all number is :",a)
            

if(b>a):
    if(b>c):
        if(b>d):
            print("The highest number along all number is :",b)

if(c>b):
    if(c>a):
        if(c>d):
            print("The highest number along all number is :",c)

if(d>b):
    if(d>c):
        if(d>a):
            print("The highest number along all number is :",d)