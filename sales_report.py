"""Generate sales report showing total melons each salesperson sold."""

# empty list for sales people
salespeople = []
# empty list for count of melons sold
melons_sold = []

# Open file to use data
f = open('sales-report.txt')
# Loop over each line in file
for line in f:
    # remove white space from end of line of text
    line = line.rstrip()
    # split up string into separate words and create list
    entries = line.split('|')

    # Get salesperson name
    salesperson = entries[0]
    # Get number of melons sold
    melons = int(entries[2])

    # if Salesperson is already in the list salespeople
    if salesperson in salespeople:
        # find the position of salesperson in salespeople list
        position = salespeople.index(salesperson)
        # increment count of melons sold
        melons_sold[position] += melons
    else:
        # Add salesperson to salespeople list
        salespeople.append(salesperson)
        # Add melon count to melons_sold list
        melons_sold.append(melons)

# for the length of the list
for i in range(len(salespeople)):
    # print how many melons were sold by each salesperson 
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')

# Improvements: refactor code into different functions:
# 1. Function for opening file and creating list from lines
# 2. Function for checking if someone is in salespeople list
# 3. Function for printing output
