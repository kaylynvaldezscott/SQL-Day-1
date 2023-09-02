fish = "halibut"

letters = []
for letter in fish:
    letters.append(letter.upper())
#print(letters)

letters=[ l.upper()     for l in fish  ]
#print(letters)


# We can also add conditional logic (if statements) to a list comprehension
july_temperatures = [87, 85, 92, 79, 106]
hot_days = []
for temperature in july_temperatures:
    if temperature > 90:
        hot_days.append(temperature)
#print(hot_days)


hot_days = [ t for t in july_temperatures if t > 90 ]  
print(hot_days)

























