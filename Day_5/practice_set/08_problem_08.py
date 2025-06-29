# If languages of two friends are same; what will happen to the program in problem 6?


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
s.update({"Harry1":a})
s.update({"Harry3":c})
s.update({"Harry4":d})
print(s)
#same values are accepted ....