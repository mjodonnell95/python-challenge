#import os
import os
#import csv
import csv
#create a path for csv
budget_csv = os.path.join('Resources','budget_data.csv')
#lists for months, profits, difference
months = []
profits = []
difference = []
#create a with statement
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    month = 0
    data = list(csvreader)
    month = len(data)
    total = 0
    firstmonth = []
    for row in data:
        months.append(row[0])
        profits.append(row[1])
    for row in range(1,len(profits)):
        x = int(profits[row]) - int(profits[row - 1])
        difference.append(x)
    total = sum(float(row[1]) for row in data)
    maximum = max(float(row[1]) for row in data)
    minimum = min(float(row[1]) for row in data)
    for (a,b) in zip(months, profits):
        if float(b) == minimum:
            minmonth = (a)
            mindecrease = (b)
        if float(b) == maximum:
            maxmonth = (a)
            maxincrease = (b)
    averagechange = round(sum(difference)/len(difference),2)
    print('Financial Analysis\n-------------------------------')
    print(f'Total Months: {month}')
    print(f'Total: $ {total}')
    print(f'Average Change: ${averagechange}')
    print('Greatest Increase in Profits: ' + str(maxmonth) + ' $' + str(maxincrease))
    print('Greatest Decrease in Profits: ' + str(minmonth) + ' $' +str(mindecrease))
