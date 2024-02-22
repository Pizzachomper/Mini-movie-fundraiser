import pandas
import random


# Currency formatting function
def currency(x):
    return f"${x:.2F}"


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

mini_movie_frame = pandas.DataFrame(mini_movie_dict)
# mini_movie_frame = mini_movie_frame.set_index('Name')

# Calculate the total ticket cost (ticket + surcharge)
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] + mini_movie_frame['Ticket Price']

# Calculate the profit for each ticket
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# Choose a winner from our name list
winner_name = random.choice(all_names)

# Get position of winner name in list
win_index = all_names.index(winner_name)

# Look up total amount won
total_won = mini_movie_frame.at[win_index, 'Total']

# Set index at end (before printing)
mini_movie_frame = mini_movie_frame.set_index('Name')
print(mini_movie_frame)

print()
print("---- Raffle Winner ----")
print(f"Congratulations {winner_name}, you have won ${total_won}, so your ticket is free!")

# Calculate the ticket and profit totals
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

# Currency Formatting (uses currency function)
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

print()
print("----- Ticket Cost / Profit -----")

# Output total ticket sales and profit
print(F"Total ticket sales: ${total:.2f}")
print(F"Total profit: ${profit:.2f}")
