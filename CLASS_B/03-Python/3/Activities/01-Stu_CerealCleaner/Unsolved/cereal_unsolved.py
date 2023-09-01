import os
import csv

cereal_csv = "01-Stu_CerealCleaner\Resources\cereal.csv"

# Open and read csv
with open(cereal_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    header=next(csv_reader)

    for r in csv_reader:
        if float(r[7])>5:
            print(r)
        






    # Read through each row of data after the header


        # Convert row to float and compare to grams of fiber
 