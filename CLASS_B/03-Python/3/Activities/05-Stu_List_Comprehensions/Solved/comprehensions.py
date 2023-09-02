names = []
for i in range(3):
    name = input("Please enter the name of someone you know. ")
    names.append(name)

print(names)

namesl = [ n.lower()  for n in names]
namesu = [ n.upper()  for n in names]
namestitlecase = [ n.title()  for n in names]


invitations = [
    f"Dear {name}, please come to the wedding this Saturday!" for name in namestitlecase]

print(invitations)


