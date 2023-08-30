import os
import csv

# Path to collect data from the Resources folder
graduation_csv = os.path.join('..', 'Resources', 'graduation_data.csv')
# Define the function and have it accept the 'state_data' as its sole parameter
# Path to collect data from the Resources folder

# Define the function and have it accept the 'state_data' as its sole parameter
def print_percentages(state_data):

    state = str(state_data[0])
    public_students = int(state_data[1])
    public_graduates = int(state_data[2])
    nonprofit_students = int(state_data[3])
    nonprofit_graduates = int(state_data[4])
    forprofit_students = int(state_data[5])
    forprofit_graduates = int(state_data[6])

    # Total students can be found by adding students of each category together
    Total_students= public_students+nonprofit_students+forprofit_students
    
    # Total graduates can be found by adding graduates of each category together
    Total_graduates=public_graduates+nonprofit_graduates+forprofit_graduates

    # Public grad rate can be found by dividing the total public graduates by the total public 
    # students and multiplying by 100
    overa_ratio=Total_graduates/Total_students*100
    pub_grad_rate= public_graduates/public_students*100
    if public_students==0:
        pub_grad_rate=0
    else:
        pub_grad_rate= public_graduates/public_students*100



   




  

# Remember that some states do not have nonprofit or forprofit private schools
# Find the non-profit school graduation rate

# Find the for-profit school graduation rate

# Calculate the overall graduation rate

# Print out the state's name and its graduation rates


# Read in the CSV file
with open(graduation_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Prompt the user for what state they would like to search for
    state_to_check = input("What state do you want to look for? ")

    # Loop through the data
    for row in csvreader:

        # If the state's name in a row is equal to that which the user input, run the 'print_percentages()' function
        if state_to_check == row[0]:
            print_percentages(row)
