# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path


# Define variables to track the financial data
total_months = 0
total_net = 0
months = []
monthly_changes = []
biggest_increase = {"month": "", "change": 0}
biggest_decrease = {"month": "", "change": 0}


# Add more variables to track other necessary financial data

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)

    # Track the total and net change
    total_months += 1
    total_net += int(first_row[1])
    previous_value = int(first_row[1])

    # Process each row of data
    for row in reader:

        # Track the total 
        total_months += 1
        current_value = int(row[1])
        total_net += current_value

        # Track the net change
        net_change = current_value - previous_value
        previous_value = current_value

        months.append(row[0])
        monthly_changes.append(net_change)

        # Calculate the greatest increase in profits (month and amount)
        if net_change > biggest_increase["change"]:
            biggest_increase["month"] = row[0]
            biggest_increase["change"] = net_change
        
        # Calculate the greatest decrease in losses (month and amount)
        if net_change < biggest_decrease["change"]:
            biggest_decrease["month"] = row[0]
            biggest_decrease["change"] = net_change

# Calculating the average net change across the months

average_change = sum(monthly_changes)/len(monthly_changes) #Sums the list of monthly changes and divides by the number of items in list 

# Generating the output summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Count of Months: {total_months}\n"
    f"Total Sum of Changes: ${total_net}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Highest Increase in Profits: {biggest_increase['month']} (${biggest_increase['change']})\n"
    f"Greatest Decrease in Profits: {biggest_decrease['month']} (${biggest_decrease['change']})\n"
)

# Print the output

print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
