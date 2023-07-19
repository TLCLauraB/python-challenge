#!/usr/bin/env python
# coding: utf-8

# Dependencies
import os
import pandas as pd
import csv


# Pathway of the CSV
election_data_path = os.path.join("Resources", "election_data.csv")

# Open the CSV
with open(election_data_path, encoding='UTF-8') as electioncsvfile:
    csv_reader = csv.reader(electioncsvfile, delimiter=",")
    
    # Read the Header Row first
    csv_header = next(csv_reader)
    
    # Test for success
    print(f"This is the Header for the CSV: {csv_header}")   

# Load CSV into Pandas data frame
df = pd.read_csv(election_data_path)

# Test for success
# print(df)

# Calculate the total number of votes in the dataset
total_votes = len(df)

# Test for sucess
# print(f"Total Votes in the dataset: {total_votes}")

# Calculate the complete list of Candidates in the dataset
total_candidates = df["Candidate"].unique()

# Test for success
# print(f"These are all the Candidates listed: {total_candidates}")

# Calculate the percentage of votes each candidate won
pcent_votes = (df.groupby("Candidate")["Candidate"].count() / df["Candidate"].count() * 100).round(3)

# Format values as percentages
pcent_votes = pcent_votes.map("{0:.3f}%".format)

# Test for success
# print(f"The percentage of votes for each {pcent_votes}")

# Calculate the total number of votes each candidate won
num_votes_per_candidate = df["Candidate"].value_counts()

# Test for success
# print(f"The total number of votes for each candidate: {num_votes_per_candidate}")

# Combining individual votes and percents into one line/output
whole_package_per_candidate = []
for candidate, pcent in pcent_votes.items():
    num_votes = num_votes_per_candidate[candidate]
    line_total = f"{candidate}: {pcent} ({num_votes})"
    whole_package_per_candidate.append(line_total)
line_totals_str = "\n".join(whole_package_per_candidate)

# Test for success
# print(f"The results of the election are:\n{line_totals_str}")

# Calculate the total number of votes each candidate won
total_votes_indi = df["Candidate"].value_counts()

# Determine the winner of the election based on popular vote
winner = total_votes_indi.idxmax()

# Test for success
# print(f"The winner of the election based on popular vote is: {winner}")

# Bringing it all together
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")
print(f"\n{line_totals_str}")
print("----------------------------")
print(f"Winner: {winner}")

# Bringing it all together + printing to a text file
with open('Analysis/election_results.txt', 'w') as f:
    print("Election Results", file=f)
    print("----------------------------", file=f)
    print(f"Total Votes: {total_votes}", file=f)
    print("----------------------------", file=f)
    print(f"\n{line_totals_str}", file=f)
    print("----------------------------", file=f)
    print(f"Winner: {winner}", file=f)

