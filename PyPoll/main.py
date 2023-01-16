# import os module, this will allow us to create file paths across operating systems
import os
#Module for reading csv files 
import csv

csvpath = os.path.join("PyPoll","Resources","election_data.csv")

#declare variables
total_votes = 0

# Create a list to hold candidates names and votes as value
candidate_votes = []
candidate_names = []

with open (csvpath) as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #Read the header row
    csv_header = next(csvreader)
       
    for row in csvreader:
        total_votes += 1 
        if row[2] in candidate_names:
            candidate_index = candidate_names.index(row[2])
            candidate_votes[candidate_index] += 1

        else:
            candidate_names.append(row[2])
            candidate_votes.append(1)
        
#Displaying Information     
print("Election Results")
print("--------------------------")
print(f'Total Votes: {total_votes}')
print("--------------------------")
for name in candidate_names:
    candidate_index = candidate_names.index(name)
    votes = (candidate_votes[candidate_index])
    percent = (votes/total_votes) *100
    print(f'{name}: {percent:.3f}% ({votes})')
print("--------------------------")
#Determine Winner with greatest votes 
greatest_votes = max(candidate_votes)
greatest_index = candidate_votes.index(greatest_votes) 
Winner = candidate_names[greatest_index] 
print(f'Winner: {Winner}')
print("--------------------------")

#Write file
output_path = os.path.join("PyPoll", "Analysis", "Output.txt")
f = open(output_path, 'w')
f.write("Election Results\n")
f.write("--------------------------\n")
f.write(f'Total Votes: {total_votes}\n')
f.write("--------------------------\n")
for name in candidate_names:
    candidate_index = candidate_names.index(name)
    votes = (candidate_votes[candidate_index])
    percent = (votes/total_votes) *100
    f.write(f'{name}: {percent:.3f}% ({votes})\n')
f.write("--------------------------\n")
#Determine Winner with greatest votes 
greatest_votes = max(candidate_votes)
greatest_index = candidate_votes.index(greatest_votes) 
Winner = candidate_names[greatest_index] 
f.write(f'Winner: {Winner}\n')
f.write("--------------------------\n")
f.close()