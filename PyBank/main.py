#!/usr/bin/env python
# coding: utf-8

# Dependencies
import os
import pandas as pd
import csv

# Pathway of the csv
budget_data_path = os.path.join("Resources", "budget_data.csv")

# Open the CSV
with open(budget_data_path, encoding='UTF-8') as budgetcsvfile:
    csv_reader = csv.reader(budgetcsvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csv_reader)
    
    # Test for success
    # print(f"This is the Header for the CSV: {csv_header}")       

# Load CSV into Pandas data frame
df = pd.read_csv(budget_data_path)

# Test for success
# print(df)

# Calculate the total number months in the dataset
total_months = len(df)

# Test for sucess
# print(f"Total Months in the dataset: {total_months}")

# Calculate the net total amount of "Profit/Losses" over the entire period of the dataset
net_total = df["Profit/Losses"].sum()

# Test for sucess
# print(f"The net total between the Profits and Losses over {total_months} months: ${net_total}")

# Calculate the changes in "Profit/Losses" over the entire period
changes = df["Profit/Losses"].diff()

# Test for sucess
# print(changes)

#Caculate the average of the changes
average_change = changes.mean().round(2)

# Test for success
# print(f"The average fluctation was: ${average_change}")

# Calculate the greatest Incresase in Profits (date and amount) over entire period
greatest_increase = changes.max()
greatest_increase_date = df.loc[changes.idxmax(), "Date"]

# Test for success
# print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")

# Calculate the greatest Decrease in Profits (date and amount) over the entire period
greatest_decrease = changes.min()
greatest_decrease_date = df.loc[changes.idxmin(), "Date"]

# Test for success
# print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Bringing it all together
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Grand Total: ${net_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")


# Bringing it all together + printing to a text file
with open('Analysis/financial_analysis.txt', 'w') as f:
    print("Financial Analysis", file=f)
    print("----------------------------", file=f)
    print(f"Total Months: {total_months}", file=f)
    print(f"Grand Total: ${net_total}", file=f)
    print(f"Average Change: ${average_change}", file=f)
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})", file=f)
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})", file=f)    


