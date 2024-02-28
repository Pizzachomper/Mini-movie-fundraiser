import pandas
import random
from datetime import date

# Dictionary to hold ticket details
all_names = ["a", "b", "c", "d", "e"]
all_ticket_costs = [7.5, 7.5, 10.50, 10.50, 6.50]
surcharge = [0, 0, 0.53, 0.53, 0]

# Dictionary used to create data frame
mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": surcharge
}

# Create frame
mini_movie_frame = pandas.DataFrame(mini_movie_dict)

# Calculate the total ticket cost (ticket + surcharge)
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] + mini_movie_frame['Ticket Price']

# Calculate the profit for each ticket
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# Calculate the ticket and profit totals
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

# Choose a winner and look up and total won
winner_name = random.choice(all_names)
win_index = all_names.index(winner_name)
total_won = mini_movie_frame.at[win_index, 'Total']

# Set index at end (before printing)
mini_movie_frame = mini_movie_frame.set_index('Name')

# Get current date for heading and filename
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%y")

heading = F" --- Mini Movie Fundraiser Ticket Data ({day}/{month}/{year}) --- "
filename = F"MMF_{year}_{month}_{day}"

# Change frame to a string, so we can export it to a file
mini_movie_string = pandas.DataFrame.to_string(mini_movie_frame)

# Create strings for printing . . .
ticket_cost_heading = "\n--- Ticket Cost / Profit ---"
total_ticket_sales = f"Total ticket sales: ${total:.2f}"
total_profit = f"Total profit: ${profit:.2f}"

# Edit text below
sales_status = "\n** All Tickets have been sold **"

winner_heading = "\n--- Raffle Winner ---"
winner_text = F"The winner of the raffle is {winner_name}. They have won ${total_won:.2f}, So their ticket is free!"

# List holding content to print / write to file
to_write = [heading, mini_movie_string, ticket_cost_heading,
            total_ticket_sales, total_profit, sales_status,
            winner_heading, winner_text]

# Print output
for item in to_write:
    print(item)

# Write output to file and create file to hold data
write_to = F"{filename}.txt"
text_file = open(write_to, "w+")

for item in to_write:
    text_file.write(item)
    text_file.write("\n")

# Close file
text_file.close()
