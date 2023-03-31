# Importing libraries to read CSV files
import os
import csv

# Storing path of CSV as variable
bankCSV = os.path.join("..", "Resources", "budget_data.csv")

date = []
pL = []

# Opening CSV file with 'csvfile', adding encoding to avoid illegal byte error
with open(bankCSV, encoding='utf') as csvfile:
    
    # Storing data from CSV as object
    bankDataReader = csv.reader(csvfile)
    # Skips header
    next(bankDataReader, None)
    for row in bankDataReader:
        date.append(row[0])

print(len(date))