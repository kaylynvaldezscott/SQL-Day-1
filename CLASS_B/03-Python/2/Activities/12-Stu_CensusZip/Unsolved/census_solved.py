import os
import csv

census_csv = os.path.join("..", "Resources", "census_starter.csv")

# Lists to store data
place = []
population = []
income = []
poverty_count = []

# * Create a Python application that reads in the data from the 2019 U.S. Census.

# * Then, store the contents of `Place`-0, `Population`-1, `Per Capita Income`-4, and `Poverty Count`-8 into Python Lists.

# * Then, zip these lists together into a single tuple.

# * Finally, write the contents of your extracted data into a CSV.