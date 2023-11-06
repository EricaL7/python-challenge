#Establish path to file
import os
import csv
election_file = os.path.join('Resources', 'election_data.csv')

 #Variables
total_votes = 0
candidates = {}
winner = {'name': '', 'votes': 0}

def format_results(total_votes, candidates):
   formatted_output = ''

   formatted_output = formatted_output + "Election Results\n"
   formatted_output = formatted_output + "----------------------------\n"
   formatted_output = formatted_output + (f"Total Votes: {total_votes}\n")
   formatted_output = formatted_output + ("----------------------------\n")

   for name, vote_count in candidates.items():
        formatted_output = formatted_output + (f"{name}: {vote_count/total_votes*100:.3f}% ({vote_count})\n")

        if winner['votes'] < vote_count:
          winner['votes'] = vote_count
          winner['name'] = name

   formatted_output = formatted_output + "----------------------------\n"

   formatted_output = formatted_output +(f"Winner: {winner['name']}\n")
   formatted_output = formatted_output + "----------------------------\n"
   
   return formatted_output


#CSV reader
with open(election_file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Skip the header row first
    csv_header = next (csvreader)

    #Total Number of votes cast
    for row in csvreader:
        total_votes = total_votes + 1

        #Complete list of candidates who received votes
        candidates_name = row[2]

        if candidates_name in candidates:
          candidates[candidates_name] = candidates[candidates_name] + 1
        else:
          candidates[candidates_name] = 1

    print(format_results(total_votes, candidates))

    #Print to txt file
with open('analysis/Election Results.txt', 'w') as text_file:
    text_file.write(format_results(total_votes, candidates))
 