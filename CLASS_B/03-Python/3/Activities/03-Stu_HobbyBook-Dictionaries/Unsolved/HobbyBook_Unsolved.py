# 1. Create a dictionary to store the following information:
# * Your name
# * Your age
# * A list of a few of your hobbies
# * A dictionary that includes a few days and the time you typically wake up on those days
d={
    "name":"Mizanur",
    "age":30,
    "hobbies":["a","b","c"],
    "wake_up":{ 

        "Sat":"7.30",
        "Sun":"6.30"
     }
}
# 2. Print out your name, how many hobbies you have, and a time you typically wake up during the week.
print((d["wake_up"]["Sat"]))

