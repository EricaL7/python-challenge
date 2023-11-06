#Establish path to file
import os
import csv
budget_data_file = os.path.join('Resources', 'budget_data.csv')

def format_results(number_of_months, net_profit_loss, average_change, greatest_increase, greatest_decrease):
   formatted_output = ''

   formatted_output = formatted_output + "Financial Analysis\n"
   formatted_output = formatted_output + "----------------------------\n"
   formatted_output = formatted_output + (f"Total Months: {number_of_months}\n")
   formatted_output = formatted_output + (f"Total: ${net_profit_loss}\n")
   formatted_output = formatted_output + (f"Average Change: ${average_change:.2f}\n")
   formatted_output = formatted_output + (f"Greatest Increase in Profits: {greatest_row_increase['date']} (${greatest_row_increase['value']})\n")
   formatted_output = formatted_output + (f"Greatest Decrease in Profits: {greatest_row_decrease['date']} (${greatest_row_decrease['value']})\n")
   return formatted_output

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

    print(format_results(number_of_months, net_profit_loss, average_change, greatest_row_increase, greatest_row_decrease))

    #Print to txt file
with open('analysis/Financial Analysis.txt', 'w') as text_file:
    text_file.write(format_results(number_of_months, net_profit_loss, average_change, greatest_row_increase, greatest_row_decrease))


    
    

    




   
   
