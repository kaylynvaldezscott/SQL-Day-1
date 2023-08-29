names = []
for _ in range(5):
    name = input("Please enter the name of someone you know. ")
    names.append(name)

# ['Mike','rahman','Rah','Piro','Ank']

# @TODO: Use a list comprehension to create a list of lowercased names
# name.lower(),name.title()
# lowercased=[]
# for name in names:
#     lowercased.append(name)

lowercased = [name.lower() for name in names]
print(lowercased)

# @TODO: Use a list comprehension to create a list of title cased names
# https://www.tutorialspoint.com/python/string_title.htm
titlecased = [name.title() for name in names]
print(titlecased)

invitations = [f"Dear {name}, please come to the wedding this Saturday!" for name in titlecased]

for invitation in invitations:
    print(invitation)
