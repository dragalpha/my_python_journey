# Check that a tuple type cannot be changed in python.

a=(1,2,3,4,5)
print(type(a))

a.sort()

# AttributeError: 'tuple' object has no attribute 'sort'