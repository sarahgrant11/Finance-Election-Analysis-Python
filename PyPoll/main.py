#import dependencies
import csv
import os

#set local computer path to data csv file
csv_file = os.path.join("PyPoll", "Resources", "election_data.csv")
analysis_file = os.path.join("PyPoll", "Analysis", "output.txt")

#create variables 
total_number = 0
candidates_dict = {}
candidates_percent = {}

#open and read csv
with open(csv_reader)
    csv_reader = csv.DictReader(Election_Data.csv)

    #skip the header row
    csv_header = next(csv_reader)
    first_row = next(csv_reader)

#read through each row of data after the header
for row in csv_reader:
    total_number = total_number + 1
    if row ['Candidate'] not in candidates_dict.keys():
        candidates_dict[row['Candidate']] = 1
    else:
        candidates_dict[row['Candidate']] = candidates_dict[row['Candidate']] + 1

# find percentage of vote for each candidate
for candidate in candidates_dict:
    candidates_percent[candidate] = round(candidates_dict[candidate] * 100 / total_number)

max_votes = 0
winner = ''

for candidate in candidates_dict:
    if candidates_ict[candidate] > max_votes: 
        max_votes = candidates_dict[candidate]
        winner = candidate

import sys
old_sysout = sys.stdoutsys.stout = open("output.txt",'w')

# print results
print("Election Results")
print("-"*10)
print("Total Votes: %d"%total_number)
print("-"*10)
for candidate in candidates_percent:
    print(candidate + ":" + "%.3f (%d)" % (candidates_percent[candidate],candidates_dict[candidate]))
print("-"*10)
print("Winner: %s"%winner)
print("-"*10)

sys.stdout = old_sysout 