#Establish path to file
import os
import csv
budget_data_file = os.path.join('Resources', 'budget_data.csv')

#CSV reader
with open(budget_data_file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #read the header row first
    csv_header = next (csvreader)

    #Variables
    number_of_months = 0
    net_profit_loss = 0
    row_profit = 0
    total_change = 0
    greatest_row_increase = {'date': '', 'value': 0}
    greatest_row_decrease = {'date': '', 'value': 0}

    #Calculate total number of months in dataset
    for row in csvreader:
        number_of_months = number_of_months + 1
        
    #Calculate net profit/loss
        net_profit_loss = net_profit_loss + int(row[1])

    #Calculate Change
        if row_profit != 0:
            row_change = (int(row[1]) - row_profit)
            total_change = total_change + row_change

        #Determine Greatest Increase in Profits
            if row_change > greatest_row_increase['value']:
                greatest_row_increase['value'] = row_change
                greatest_row_increase['date'] = row[0]

         #Determine Greatest Increase in Profits
            if row_change < greatest_row_decrease['value']:
                greatest_row_decrease['value'] = row_change
                greatest_row_decrease['date'] = row[0]

    #Set row_profit to current row's profit
        row_profit = int(row[1])

    #calculate average change
    total_number_of_changes = number_of_months-1
    average_change = total_change/total_number_of_changes

    #Print Statement
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {number_of_months}")
    print(f"Total: ${net_profit_loss}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_row_increase['date']} (${greatest_row_increase['value']})")
    print(f"Greatest Decrease in Profits: {greatest_row_decrease['date']} (${greatest_row_decrease['value']})")




   
   
