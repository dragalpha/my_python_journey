# Write a program to input eight numbers from the user and display all the unique
# numbers (once).
a=set()
for n in range(1,9):
    a1=int(input(f"Enter number {n}:\t"))
    a.add(a1)
print(a)