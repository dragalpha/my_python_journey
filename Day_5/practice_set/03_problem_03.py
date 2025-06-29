# Can we have a set with 18 (int) and '18' (str) as a value in it?
a={18,"18"}
a1=list(a)
print(a)
print(type(a))
print(type(a1))
print(type(a1[0]))
print(type(a1[1]))
