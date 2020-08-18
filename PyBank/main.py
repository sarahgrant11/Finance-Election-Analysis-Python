#import dependencies
import csv 
import os

#set local computer path to data csv file
csv_file = os.path.join("PyBank", "Resources", "Budget_Data.csv")
analysis_file = os.path.join("PyBank", "Analysis", "output.txt")

#create variables
month = 0
profit = 0
net_change_list = []
month_change = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999] 

#open and read csv
with open(csv_file) as Financial_Data:   
    csv_reader = csv.reader(Financial_Data)

    #skip the header row
    csv_header = next(csv_reader)
    first_row = next(csv_reader)

    month = month + 1
    profit = profit + int(first_row[1])
    previous_net = int(first_row[1])

    #read through each row of data after the header
    for row in csv_reader:
        month = month + 1
        profit = profit + int(row[1])
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        month_change = month_change + [row[0]] 

        # Tracking greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        # Tracking greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change       

#Calculate the net changes 

average_monthly_net = sum(net_change_list) / len(net_change_list)

#Print Statements
output = (
    f"Financial Analysis \n"
    f"----------------------------\n"
    f"Total Months: {month}\n"
    f"Total: {profit}\n"
    f"Average Change: {average_monthly_net}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print(output)
# Export the results to text file
with open(analysis_file, "w") as txt_file:
    txt_file.write(output)
