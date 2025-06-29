# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

s=[]
for n in range (1,4):
    a=int(input(f"Enter subject {n}:"))
    s.append(a)
print("The Number of consicutive Subjects :",s)
s1=sum(s)/3
print("The Sum of Three Consicutive numbers:\t",s1)

if s[0]<33 or s[1]<33 or s[2]<33:
    print("Fail !!!!!!!!!")
elif s1<40:
    print("Fail !!!!!!!!!")
else:
    print("Pass!!!!!!!!!")

