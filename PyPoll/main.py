#import os module to create file paths across operating systems
import os

# import module for reading csv files
import csv

# Identify the file path
csv_path = os.path.join('Resources', 'election_data.csv')

NumberOfVotes = 0
NumberOfCandidates = 0

#Create list to store candidates
Candidates = []

#Create list to store candidate column
CandidateCol = []

#Create a list to store the votes for each candidate in the Candidates list
CandidateVotes = []

#Create a list to store the percentage votes for each candidate in the Candidates list
PercentageOfVotes = []

with open(csv_path, encoding='UTF-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first 
    csv_header = next(csv_file)

    # Read through each row of data after the header
    for row in csv_reader:

        #Count number of votes. This is the same as counting the number of rows in this case.
        NumberOfVotes = NumberOfVotes + 1

        #Create list of the Candidate column 
        CandidateCol.append(row[2])

        #Add candidates to Candidates list
        if row[2] not in Candidates:
            Candidates.append(row[2])

    NumberOfCandidates = len(Candidates)

    for i in range(NumberOfCandidates):

        # For each candidate, add the number of times they appear in the candidate column to the CandidateVotes list
        CandidateVotes.append(CandidateCol.count(Candidates[i]))

        # Calculate the percentage of votes for each candidate and add it to the PercentageOfVotes list
        PercentageOfVotes.append(CandidateVotes[i]/NumberOfVotes)
    
    # Find the index of the max number of votes and the name that correlates to that index in the Candidates list 
    ElectionWinner = Candidates[CandidateVotes.index(max(CandidateVotes))]

# Print the results to the terminal

print("Election Results")
print("------------------------------------------")
print(f" Total Votes: {NumberOfVotes}")
print("------------------------------------------")
for i in range (0,NumberOfCandidates): 
        print(f"{Candidates[i]}: {PercentageOfVotes[i] : .3%} ({CandidateVotes[i]})")
print("----------------------------")
print(f"Winner: {ElectionWinner}")
print("----------------------------")

# Write findings to txt file
# Specify the file to write to
output_path = os.path.join("Election Results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:
    txtfile.write("Election Results")
    txtfile.write("\n")
    txtfile.write("------------------------------------------")
    txtfile.write("\n")
    txtfile.write(f" Total Votes: {NumberOfVotes}")
    txtfile.write("\n")
    txtfile.write("------------------------------------------")
    txtfile.write("\n")
    for i in range (0,NumberOfCandidates): 
        txtfile.write(f"{Candidates[i]}: {PercentageOfVotes[i] : .3%} ({CandidateVotes[i]})")
        txtfile.write("\n")
    txtfile.write("----------------------------")
    txtfile.write("\n")
    txtfile.write(f"Winner: {ElectionWinner}")
