import os
import csv

#state_data=[Alabama,19556,9643,4666,2041,669,336]
graduation_csv ="08-Par_GraduatingFunctions\Resources\graduation_data.csv" 

def print_percentages(state_data):
    #get the values from the data
    state=str(state_data[0])
    public_students=int(state_data[1])
    public_graduates = int(state_data[2])
    nonprofit_students = int(state_data[3])
    nonprofit_graduates = int(state_data[4])
    forprofit_students = int(state_data[5])
    forprofit_graduates = int(state_data[6])

    total_students = public_students + nonprofit_students + forprofit_students

    total_graduates = public_graduates + nonprofit_graduates + forprofit_graduates

    overall_grad_rate = (total_graduates / total_students) * 100

    public_grad_rate = (public_graduates / public_students) * 100

    if nonprofit_students == 0:
        nonprofit_grad_rate = 0
    else:
        nonprofit_grad_rate = (nonprofit_graduates / nonprofit_students) * 100

    if forprofit_students == 0:
        forprofit_grad_rate = 0
    else:
        forprofit_grad_rate = (forprofit_graduates / forprofit_students) * 100

    if overall_grad_rate > 50:
        message = "Graduation success"
    else:
        message = "State needs improvement"

     # Print out the state's name and their graduation rates
    print(f"Stats for {state}")
    print(f"Public School Graduation Rate: {str(public_grad_rate)}")
    print(f"Private Non-Profit School Graduation Rate: {str(nonprofit_grad_rate)}")
    print(f"Private For-Profit School Graduation Rate: {str(forprofit_grad_rate)}")
    print(f"Overall Graduation Rate: {str(overall_grad_rate)}")
    print(f"{message}")


with open(graduation_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        print(row)
        print_percentages(row)
        
       
        















    









































