import pandas
import random
from datetime import date


# Functions go here
# Checks that user response is not blank
def not_blank(question):
    while True:
        response = input(question)

        # If response is blank output error
        if response == "":
            print("Sorry this can't be blank. Please try again")

        else:
            return response


# Checks users enter an integer to a given question
def num_check(question):
    while True:
        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter an integer")
            print()


# Calculate the ticket price based on the age
def calc_ticket_price(var_age):
    # Ticket is $7.5 for users under 16
    if var_age < 16:
        price = 7.5

    # Ticket is $10 for users between 16 and 64
    elif var_age < 65:
        price = 10.5

    # Ticket price is $6.50 for seniors (65+)
    else:
        price = 6.5

    return price


# Checks that users enter a valid response
# Cash / credit based on a list of options
def string_checker(question, num_letters, valid_responses):
    error = f"Please choose {valid_responses[0]} or {valid_responses[1]}"

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        print(error)
        print()


# Currency formatting function
def currency(x):
    return f"${x:.2f}"


# Main routine

# Set maximum number of tickets below
MAX_TICKETS = 5
tickets_sold = 0

# Lists below
yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

# Dictionary to hold ticket details
all_names = []
all_ticket_costs = []
all_surcharge = []

# Dictionary used to create data frame
mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": all_surcharge
}

# Ask user if they want to see instructions
want_instructions = string_checker("Do you want to read the instructions (y/n): ", 1, yes_no_list)

if want_instructions == "yes" or want_instructions == "y":
    print('''\n
*** Instructions ***

For each ticket, enter . . .
- The person's name (Cant be blank)
- Age (Between 12 and 120)
- Payment method (cash / credit)

When you have entered all the users, press 'xxx' to quit.

The program will then display the ticket details
Including the cost of each ticket, the total cost and the total profit.

This information will automatically written to a text file.

*********************''')

print()

# Loop to sell tickets
tickets_sold = 0
while tickets_sold < MAX_TICKETS:
    name = not_blank("Enter your name (or 'xxx' to quit): ")

    if name == 'xxx' and len(all_names) > 0:
        break

    elif name == 'xxx':
        print("You must sell at least one ticket before quitting")
        continue

    age = num_check("What is your age?: ")

    if 12 <= age <= 120:
        pass

    elif age < 12:
        print("Sorry you are too young for this movie")
        continue

    else:
        print("That looks like a typo, please try again")
        continue

    # Calculate ticket cost
    ticket_cost = calc_ticket_price(age)

    # Get payment method
    pay_method = string_checker("Choose a payment method (cash or credit): ", 2, payment_list)
    print()

    if pay_method == "cash":
        surcharge = 0
    else:
        # Calculate 5% surcharge if users are playing by credit card
        surcharge = ticket_cost * 0.05

    tickets_sold += 1

    # Add ticket name, cost and surcharge to lists
    all_names.append(name)
    all_ticket_costs.append(ticket_cost)
    all_surcharge.append(surcharge)

# Create data from dictionary to organise information
mini_movie_frame = pandas.DataFrame(mini_movie_dict)
# mini_movie_frame = mini_movie_frame.set_index('Name')

# Calculate the total ticket cost (ticket + surcharge)
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] + mini_movie_frame['Ticket Price']

# Calculate the profit for each ticket
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# Calculate the ticket and profit totals
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

# Currency Formatting (uses currency function)
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

# Choose a winner from our name list
winner_name = random.choice(all_names)
win_index = all_names.index(winner_name)
total_won = mini_movie_frame.at[win_index, 'Total']

# Set index at the end (before printing)
mini_movie_frame = mini_movie_frame.set_index('Name')

# Get current date for heading and filename
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%y")

heading = F"\n--- Mini Movie Fundraiser Ticket Data ({day}/{month}/{year}) ---\n"
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
winner_text = f"The winner of the raffle is {winner_name}. They have won {total_won}, So their ticket is free!"

# List holding content to print / write to file
print()
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

# Output number of tickets sold
if tickets_sold == MAX_TICKETS:
    print("Congratulations you have sold all the tickets")

else:
    print(F"You have sold {tickets_sold} ticket/s. There is {MAX_TICKETS - tickets_sold} remaining.")
