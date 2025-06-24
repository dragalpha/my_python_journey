# Check the type of variable assigned using input () function.
a=input("Enter Anything:")
try:
    a=int(a)
except ValueError:
    try:
        a=float(a)
    except ValueError:
        pass
print("The typr of a:", type(a)) 
