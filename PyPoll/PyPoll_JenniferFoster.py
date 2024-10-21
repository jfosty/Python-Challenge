# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Defining lists and dictionaries to track candidate names and vote counts
vote_count = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_counter = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Increment the total vote count for each row
        total_votes +=1 #new variable for counting votes

        # Get the candidate's name from the row
        candidate_name = row[2] # save candidate name value in list


        # If the candidate is not already in the candidate list, add them
        if candidate_name not in vote_count:
            vote_count[candidate_name] = 0 # candidate name was not in list so we know this candidate has 0 votes

        # Add a vote to the candidate's count
        vote_count[candidate_name] += 1 


# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Write the total vote count to the text file
    results = (f"\nElection Results\n"
        f"----------------------\n"
        f"Total Votes: {total_votes}\n"
        f"----------------------\n")

    # Print the total vote count (to terminal)
    print(results)
    txt_file.write(results)

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate, candidate_votes in vote_count.items():

        # Get the vote count and calculate the percentage
        vote_percentage = (candidate_votes/total_votes)*100 

        # Update the winning candidate if this one has more votes
        if candidate_votes > winning_counter:
            winning_counter  = candidate_votes
            winning_candidate = candidate
        # Print and save each candidate's vote count and percentage

        candidate_results = f"{candidate}: {vote_percentage:.3f}% ({candidate_votes})\n"
        print(candidate_results, end = "")
        txt_file.write(candidate_results)

    # Generate and print the winning candidate summary
    winning_announcement = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n"
    )

    # Save the winning candidate summary to the text file
    print(winning_announcement)
    txt_file.write(winning_announcement)