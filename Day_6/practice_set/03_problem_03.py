# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams.
spam_keyword=["make a lot of money", "buy now", "subscribe this", "click this"]
comment=input("Enter Your Comment:\t").lower()
if any(keyword in comment for keyword in spam_keyword):
    print("Spam Found")
else:
    print("Real Deal")
