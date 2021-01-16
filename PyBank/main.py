import os
import csv
import sys

# Create path to file: budget_data.csv
budget_csv = os.path.join( "Resources", "budget_data.csv")

# Open path created.
with open(budget_csv) as budget:

    # Read file to a df, named rows.
    rows = csv.reader(budget)

    next(rows, None) # Skip headers
    
    # Initialize variables
    months = 0
    result = 0
    lastrowresult = 0
    totalresults = 0
    change = 0

    for row in rows: 

        if months == 0:                         # If it is the first iteration
            greatestincrease = 0                # do not calculate increases nor
            greatestdecrease = 0                # decreases.

        else:
            result = int(row[1])-int(lastrowresult)     # Calculate the first difference
            change = change + result                    # between month's results
            if (result > greatestincrease):             
                greatestincrease=result                 # If difference is the biggest, save info.
                greatestincrease_month = row[0]
            if (result < greatestdecrease):
                greatestdecrease=result                 # If difference is the lowest, save info.
                greatestdecrease_month = row[0]
         
        totalresults = int(totalresults)+int(row[1])    # Aggregates the result to total results.
        lastrowresult = row[1]
        months = months + 1

    print(" ----------------------------------------")
    print("             Financial Analysis")
    print(" ----------------------------------------")
    print (f'Total Months       : ${months}')
    print (f'Total              : ${totalresults}')
    print (f'Total              : ${totalresults}')
    print (f'Average Change     : ${round(change/(months-1),2)}')
    print (f'Greatest Increase in Profits: {greatestincrease_month}, ( ${greatestincrease})')
    print (f'Greatest Decrease in Profits: {greatestdecrease_month}, ( ${greatestdecrease})')

# Create path to file to write results.
analysis_file = os.path.join( "Analysis", "analysis.txt")
with open(analysis_file, 'w') as f:
    sys.stdout = f
    print(" ----------------------------------------")
    print("             Financial Analysis")
    print(" ----------------------------------------")
    print (f'Total Months       : ${months}')
    print (f'Total              : ${totalresults}')
    print (f'Total              : ${totalresults}')
    print (f'Average Change     : ${round(change/(months-1),2)}')
    print (f'Greatest Increase in Profits: {greatestincrease_month}, ( ${greatestincrease})')
    print (f'Greatest Decrease in Profits: {greatestdecrease_month}, ( ${greatestdecrease})')
    sys.stdout = original_stdout
