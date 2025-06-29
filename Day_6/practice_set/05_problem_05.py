# Write a program which finds out whether a given name is present in a list or not.
name_keyword=["ram", "shyam","jadu","madhu"]

username=input("Enter your name \t").lower()

if any(keyword in username for keyword in name_keyword):
    print("Valid!")
else:
    print("Invalid")