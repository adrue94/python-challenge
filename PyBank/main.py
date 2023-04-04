# Importing libraries to read CSV files
import os
import csv
import numpy

# Storing path of CSV as variable(?) / object(?)
bankCSV = os.path.join("Resources", "budget_data.csv")
output_Path = os.path.join("Analysis", "Analysis.txt")

# Initializing lists, variables, etc.
date = []
pl_List = []
pl_Diff = []

# Opening CSV file with 'csvfile', add encoding to avoid illegal byte error
with open(bankCSV, encoding='utf-8') as csvfile:
    
    # Storing data from CSV as object
    bankDataReader = csv.reader(csvfile)
    next(bankDataReader)
    # Populating date and pl_List with respective rows; making sure pl_List is held as int
    for row in bankDataReader:
        date.append(row[0])
        pl_List.append(int(row[1]))

    # Grabbing necessary variables from lists; total, averages, max and min
    # Using numpy to easily find difference in adjacent values of list, thanks stackoverflow!
    # Populating another list with the difference to better mainpulate data
    pl_Total = sum(pl_List)
    pl_Diff = numpy.diff(pl_List)

    pl_Avg = sum(pl_Diff)/len(pl_List)
    gIncrease = max(pl_Diff)
    indexMax = numpy.argmax(pl_Diff) + 1
    gDecrease = min(pl_Diff)
    indexMin = numpy.argmin(pl_Diff) + 1
    # As numpy.diff finds the difference of two adjacent values, it will return (n - 1) values from a list
    # We add (+ 1) to reflect the month after the change occurred

print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {len(date)}')
print(f'Total: ${pl_Total}')
print(f'Average Change: ${pl_Avg}')
print(f'Greatest Increase in Profits: {date[indexMax]} (${gIncrease})')
print(f'Greatest Decrease in Profits: {date[indexMin]} (${gDecrease})')

with open(output_Path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['----------------------------'])
    csvwriter.writerow([f'Total Months: {len(date)}'])
    csvwriter.writerow([f'Total: ${pl_Total}'])
    csvwriter.writerow([f'Average Change: ${pl_Avg}'])
    csvwriter.writerow([f'Greatest Increase in Profits: {date[indexMax]} (${gIncrease})'])
    csvwriter.writerow([f'Greatest Decrease in Profits: {date[indexMin]} (${gDecrease})'])