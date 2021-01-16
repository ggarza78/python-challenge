import os
import csv
import sys

# Create path to file: election_data.csv
election_csv = os.path.join( "Resources", "election_data.csv")

# Open path created.
with open(election_csv) as election:

    # Read file to a df, named rows.
    rows = csv.reader(election)

    next(rows, None) # Skip headers
    
    # Initialize variables
    candidates = []
    votes = []
    totalvotes = 0

    for row in rows:    # row has a structure with Voter ID, County, Candidate
        # Look for the candidate in the list
        try:
            index_candidate = candidates.index(row[2])
        except ValueError:
            index_candidate = -1                            # if not found, designate -1

        if(index_candidate>=0):                             # if candidate already exists
            votes[index_candidate]=votes[index_candidate]+1 # add 1 to votes
        else:
            index_candidate=len(candidates)             # if it is a new candidate
            candidates.append(row[2])                   # append the name
            votes.append(1)                             # and a new vote
        totalvotes = totalvotes + 1                     # Sum the total of votes + 1


    percentages = []
    greatestindex = 0
    greatestnumber = 0
    counter = 0

    for x in votes:                                     # For every entry in list votes        
        percentages.append(round(x*100/totalvotes,3))   # create a ew entry on
        if (greatestnumber<x):                          # percentages list
            greatestnumber = x
            greatestindex = counter
        counter = counter + 1


print(" ----------------------------------------")
print("             Election Results")
print(" ----------------------------------------")
print(f" Total Votes         : {totalvotes}")
print(" ----------------------------------------")
counter = 0
for x in candidates:
    print (f' {candidates[counter]}:    {percentages[counter]}% ({votes[counter]})')
    counter = counter + 1
print(" ----------------------------------------")
print(f" Winner      : ** {candidates[greatestindex]} ** ")

# Create path to file to write results.
analysis_file = os.path.join( "Analysis", "analysis.txt")
with open(analysis_file, 'w') as f:
    sys.stdout = f 
    print(" ----------------------------------------")
    print("             Election Results")
    print(" ----------------------------------------")
    print(f" Total Votes         : {totalvotes}")
    print(" ----------------------------------------")
    counter = 0
    for x in candidates:
        print (f' {candidates[counter]}:    {percentages[counter]}% ({votes[counter]})')
        counter = counter + 1
    print(" ----------------------------------------")
    print(f" Winner      : ** {candidates[greatestindex]} ** ")
    #sys.stdout = original_stdout