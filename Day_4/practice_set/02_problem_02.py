# Write a program to accept marks of 6 students and display them in a sorted
# manner.

a=[]
for n in range (1,7):
    a1=int(input(f"Number of student{n}:"))
    a.append(a1)
print("The unsorted number :",a)
a.sort()
print("The sorted number :",a)