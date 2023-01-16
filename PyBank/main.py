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
greatest_inc_month = ""
greatest_dec_month = ""
dates = [] 

with open (csvpath) as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #Read the header row
    csv_header = next(csvreader)
#process the first row to obtain inital values 
    first_row = next(csvreader)
    months += 1
    net_total = net_total + int(first_row[1])
    previous_month = int(first_row[1])
    dates.append(first_row[0])
    
    for row in csvreader:
        #Total number of months
        months = months + 1
        net_total = net_total + int(row[1])
        profit_loss_change.append(int(row[1])- previous_month)
        previous_month = int(row[1])
        average_change = (sum(profit_loss_change))/(len(profit_loss_change))
        dates.append(row[0])
#Greatest Increase /Index increased by 1 to account for first row
greatest_inc = max(profit_loss_change)
greatest_index = profit_loss_change.index(greatest_inc) + 1
greatest_inc_month = dates[greatest_index]

#Greatest Decrease /Index increased by 1 to account for first row
greatest_dec = min(profit_loss_change)
worst_index = profit_loss_change.index(greatest_dec) + 1
greatest_dec_month = dates[worst_index]

#Displaying Information     
print("Financial Analysis")
print("--------------------------")
print(f'Total Months: {months}')
print(f'Total: ${net_total}')
print("Average Change: $" + str(round(average_change, 2)))
print(f'Greatest Increase in Profits: {greatest_inc_month} (${greatest_inc})')
print(f'Greatest Decrease in Profits: {greatest_dec_month} (${greatest_dec})')

#write file 
output_path = os.path.join("PyBank", "Analysis", "Output.txt")
f = open(output_path, 'w')
f.write("Financial Analysis\n")
f.write("--------------------------\n")
f.write(f'Total Months: {months}\n')
f.write(f'Total: ${net_total}\n')
f.write("Average Change: $" + str(round(average_change, 2)) + "\n")
f.write(f'Greatest Increase in Profits: {greatest_inc_month} (${greatest_inc})\n')
f.write(f'Greatest Decrease in Profits: {greatest_dec_month} (${greatest_dec})\n')
f.close()
