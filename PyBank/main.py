# import os module, this will allow us to create file paths across operating systems
import os
#Module for reading csv files 
import csv

csvpath = os.path.join("PyBank","Resources","budget_data.csv")
#declare variables 
months = 0
net_total = 0
profit_loss_change = []
change = 0 
previous_month = 0
average_change = 0.0

with open (csvpath) as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #Read the header row
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    first_row = next(csvreader)
    months += 1
    net_total = net_total + int(first_row[1])
    previous_month = int(first_row[1])

    
    for row in csvreader:
        months = months + 1
        net_total = net_total + int(row[1])
        profit_loss_change.append(int(row[1])- previous_month)
        previous_month = int(row[1])
        average_change = (sum(profit_loss_change))/(len(profit_loss_change))


print("Financial Analysis")
print("--------------------------")
print(f'Total Months: {months}')
print(f'Total: ${net_total}')
print(f'Average Change: ${average_change}')
