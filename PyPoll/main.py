# Importing libraries to read CSV files
import os
import csv
import numpy

# Storing path of CSV as variable(?) / object(?)
pollCSV = os.path.join("Resources", "election_data.csv")
output_Path = os.path.join("Analysis", "Poll_Analysis.txt")

# Initializing lists
indID = []
indCou = []
indCand = []

# Opening CSV file with 'csvfile', add encoding to avoid illegal byte error
with open(pollCSV, encoding='utf-8') as csvfile:
    
    # Storing data from CSV as object, skips header
    pollDataReader = csv.reader(csvfile)
    pollDataHeader = next(pollDataReader)
   # Populating lists with data from respective rows 
    for row in pollDataReader:
        indID.append(row[0])
        indCou.append(row[1])
        indCand.append(row[2])

# Using 'set()' to find unique candidates, then turning it back to list
setCand = set(indCand)
listCand = list(setCand)

# Using 'len()' to find votes casted
totVotes = len(indID)

# Using 'count()' to find total duplicates in list 'indCand'; finds total votes for each candidate
# Then calculates percentage of all votes 
FiCandVotes = indCand.count(listCand[0])
fcvPer = (FiCandVotes / totVotes)*100
SeCandVotes = indCand.count(listCand[1])
scvPer = (SeCandVotes / totVotes)*100
ThCandVotes = indCand.count(listCand[2])
tcvPer = (ThCandVotes / totVotes)*100

# Puts total votes of each candidates into list 'winVote' in seq. order
candRecVotes = [FiCandVotes, SeCandVotes, ThCandVotes]
# Using 'numpy.argman()' to find the highest number and its position in list 'winVote' 
winVote = numpy.argmax(candRecVotes)


print(f'Election Results')
print(f'-------------------------')
print(f'Total Votes: {totVotes}')
print(f'-------------------------')
print(f'{listCand[0]}: {fcvPer:.3f}% ({FiCandVotes})')
print(f'{listCand[1]}: {scvPer:.3f}% ({SeCandVotes})')
print(f'{listCand[2]}: {tcvPer:.3f}% ({ThCandVotes})')
print(f'-------------------------')
# As the votes were put in the list in sequential order, we can find the candidate with highest votes
print(f'Winner: {listCand[winVote]}')
print(f'-------------------------')

with open(output_Path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['-------------------------'])
    csvwriter.writerow([f'Total Votes: {totVotes}'])
    csvwriter.writerow([f'-------------------------'])
    csvwriter.writerow([f'{listCand[0]}: {fcvPer:.3f}% ({FiCandVotes})'])
    csvwriter.writerow([f'{listCand[1]}: {scvPer:.3f}% ({SeCandVotes})'])
    csvwriter.writerow([f'{listCand[2]}: {tcvPer:.3f}% ({ThCandVotes})'])
    csvwriter.writerow([f'-------------------------'])
    csvwriter.writerow([f'Winner: {listCand[winVote]}'])
    csvwriter.writerow([f'-------------------------'])


# There should be a smarter way to do this; maybe a dict sorted by candidate and their associated votes
# Then we just print each key / candidate in the dict
# The only problem would be sorting by votes received and outputting data without brackets.

# candDict = {
#     'First Candidate': [listCand[0], fcvPer, FiCandVotes],
#     'Second Candidate': [listCand[1], scvPer, SeCandVotes],
#     'Third Candidate': [listCand[2], tcvPer, ThCandVotes]
# }