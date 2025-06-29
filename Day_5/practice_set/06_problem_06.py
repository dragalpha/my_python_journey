# Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.
s={
    "Harry":"",
    "Harry1":"",
    "Harry3":"",
    "Harry4":"",
}
a=input("Enter the Favourite subject of harry:")
b=input("Enter the Favourite subject of harry1:")
c=input("Enter the Favourite subject of harry3:")
d=input("Enter the Favourite subject of harry4:")
s.update({"Harry":a})
s.update({"Harry1":b})
s.update({"Harry3":c})
s.update({"Harry4":d})
print(s)
