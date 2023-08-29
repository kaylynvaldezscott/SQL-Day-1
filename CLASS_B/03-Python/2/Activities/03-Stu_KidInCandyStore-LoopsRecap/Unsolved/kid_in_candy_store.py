# The list of candies to print to the screen
candy_list = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish", "Skittles", "Hershey Bar", "Starbursts", "M&Ms"]

# The amount of candy the user will be allowed to choose
allowance = 5

# The list used to store all of the candies selected inside of
candy_cart = []

# Print out options
#1. Print all of the candies to the screen and their index in brackets
for i in candy_list:
    print(candy_list.index(i), i)

for index,candy in enumerate(candy_list):
    print(index,candy)

#Run through a loop which allows the user to choose which candies to take home with them
#print("Which candy would you like to bring home?")
for i in range(allowance):
    s=int(input())
    candy_cart.append(candy_list[s])





    # Add the candy at the index chosen to the candy_cart list
    

# Loop through the candy_cart to say what candies were brought home


