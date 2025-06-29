# Write a program to find out whether a given post is talking about “Harry” or not.

required_keyword=["harry",]
comment=input("Enter the comment :\t").lower()

if any(keyword in comment for keyword in required_keyword):
    print("Valid!")
else:
    print("Invalid !!")