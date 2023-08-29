# Take input of you and your neighbor
your_first_name = input("What is your name? ")
neighbor_first_name = input("What is your neighbor's name? ")

# Take how long each of you have been coding
months_you_coded = int(input( ))
months_neighbor_coded = int(input())

# Add total month
total_months_coded = months_you_coded + months_neighbor_coded

# Print results
print("I am " + your_first_name + " and my neighbor is " + neighbor_first_name)
print("Together we have been coding for " + str(total_months_coded) + " months!")
print(f"Together we have been coding for  + {total_months_coded} + months!")