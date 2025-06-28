letter ='''
            Dear |<Name>|,
                        You are Selected
                                        |<Date>|'''

a=input("What Is Your Name:")
b=input("Enter the Date you wanna Admitted:")
# letter=letter.replace("|<Name>|",a )

# letter=letter.replace("|<Date>|",b )
# print(letter)

print(letter.replace("|<Name>|",a).replace("|<Date>|",b))