# Write a program to sum a list with 4 numbers.
a=[]
for n in range(1,5):
    a1=int(input((f"enter number {n}:")))
    a.append(a1)
print("The Entered 4 numbers:",a)
print("Sum of 4 numbers",sum(a))