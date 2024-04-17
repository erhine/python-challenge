#import os module to create file paths across operating systems
import os

# import module for reading csv files
import csv

# Identify the file path
csv_path = os.path.join('Resources', 'budget_data.csv')

# set variables
NumberOfMonths = 0
NetProfit = 0
ChangeInProfit = 0
GreatestIncreaseAmount = 0
GreatestIncreaseMonth = ''
GreatestDecreaseAmount = 0
GreatestDecreaseMonth = ''

# create list to hold the months
Months = []

# create two lists, one to store the profit amounts and another to track month to month changes in profit
ProfitList = []
ProfitChangeList = []


with open(csv_path, encoding='UTF-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first 
    csv_header = next(csv_file)

    # Read through each row of data after the header
    for row in csv_reader:

        #count number of months
        NumberOfMonths = NumberOfMonths + 1

        #add profit/loss
        NetProfit = NetProfit + int(row[1])

        #add the months to the Months list and  profit amounts to ProfitList
        Months.append(row[0])
        ProfitList.append(int(row[1]))

    # Iterate through Profit list to find change in profits
    for i in range(len(ProfitList)-1):
        
        #Add the change between the current month and the previous month to the ProfitChangeList
        ProfitChangeList.append(ProfitList[i+1] - ProfitList[i])

# Find the maximum and minmum amounts in the ProfitChangeList
GreatestIncreaseAmount = max(ProfitChangeList)
GreatestDecreaseAmount = min(ProfitChangeList)

# Find which month in the Months list the max and min of ProfitChangeList correlate to
GreatestIncreaseMonth = Months[ProfitChangeList.index(GreatestIncreaseAmount)+1]
GreatestDecreaseMonth = Months[ProfitChangeList.index(GreatestDecreaseAmount)+1]


# Calculate the average profit change but summing up all items in the Profit Change List, dividing by the number of items, and rouding to 2 decimal places
AverageProfitChange = round(sum(ProfitChangeList)/len(ProfitChangeList),2)


        
# Print out findings to terminal
print("Financial Analysis")
print("------------------------------------------")
print(f"Total Months: {NumberOfMonths}")
print(f"Total: ${NetProfit}")
print(f"Average Change: ${AverageProfitChange}")
print(f"Greatest Increase in Profits: {GreatestIncreaseMonth} (${GreatestIncreaseAmount})")
print(f"Greatest Decrease in Profits: {GreatestDecreaseMonth} (${GreatestDecreaseAmount})")

# Write findings to txt file
# Specify the file to write to
output_path = os.path.join("Financial Results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:

    txtfile.write("Financial Analysis")
    txtfile.write("\n")
    txtfile.write("------------------------------------------")
    txtfile.write("\n")
    txtfile.write(f"Total Months: {NumberOfMonths}")
    txtfile.write("\n")
    txtfile.write(f"Total: ${NetProfit}")
    txtfile.write("\n")
    txtfile.write(f"Average Change: ${AverageProfitChange}")
    txtfile.write("\n")
    txtfile.write(f"Greatest Increase in Profits: {GreatestIncreaseMonth} (${GreatestIncreaseAmount})")
    txtfile.write("\n")
    txtfile.write(f"Greatest Decrease in Profits: {GreatestDecreaseMonth} (${GreatestDecreaseAmount})")
