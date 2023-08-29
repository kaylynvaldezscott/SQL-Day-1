# 1. Create a dictionary to store the following information:
# * Your name
# * Your age
# * A list of a few of your hobbies
# * A dictionary that includes a few days and the time you typically wake up on those days

my_info = {"name": "Rex",
           "occupation": "dog",
           "age": 21,
           "hobbies": ["barking", "eating", "sleeping", "loving my owner"],
           "wake-up": {"Mon": 5, "Friday": 5, "Saturday": 10, "Sunday": 9}}

# 2. Print out your name, how many hobbies you have, and a time you typically wake up during the week.

print(my_info['name'])
print(my_info['occupation'])
print(len(my_info['hobbies']))

my_info['wake-up']['Mon']