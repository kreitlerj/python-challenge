#PyBank Challenge

#Import modules os and csv
import os
import csv

#Creating lists to store data
months = []
profit_loss = []

#Set path for the file
budget_csv = os.path.join('budget_data.csv')

#Open the CSV
with open(budget_csv, newline="") as csvfile:
    budget_reader = csv.reader(csvfile, delimiter=",")

    #Skip the header row
    next(budget_reader)

    #Loop through the CSV file
    for row in budget_reader:

        #Add date
        months.append(row[0])

        #Add Profit/Loss
        profit_loss.append(float(row[1]))

#Calculate the total months included in the data set
total_months = (len(months))

#Calculate the net amount of Profit/Losses over the period of time
net_amount = sum(profit_loss)

#Calculate the average change per month
avg_change = net_amount / total_months

#Calculate the greatest increase in profits (date and amount)
max_profit = max(profit_loss)

#Using the index of the greatest increase to find the date
index_max = profit_loss.index(max_profit)
max_month = months[index_max]

#Calculate the greatest decrease in loss (date and amount)
min_profit = min(profit_loss)

#Using the index of the greatest decrease to find the date
index_min = profit_loss.index(min_profit)
min_month = months[index_min]

financial_analysis = (f'''Financial Analysis
----------------------------------
Total Months: {total_months}
Total: ${net_amount:.2f}
Average Change: {avg_change:.2f}
Greatest Increase in Profits: {max_month} {max_profit:.2f}
Greatest Decrease in Profits: {min_month} {min_profit:.2f}''')

#Print out analysis
print(financial_analysis)

#Create a .txt file containing the same analysis in the print out
analysis = open('financial_analysis.txt', 'w')

analysis.write(financial_analysis)

analysis.close()