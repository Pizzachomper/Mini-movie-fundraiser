#Functions go here
#Checks that user response is not blank
def not_blank(question):
    while True:
        response = input(question)

        #If response is blank output error
        if response == "":
            print("Sorry this can't be blank. Please try again")

        else:
            return response

#Checks users enter an integer to a given question
def num_check(question):
    while True:
        try:
            response = int(input(question))
            return response
        
        except ValueError:
            print("Please enter an integer")
            print()

#Calculate the ticket price based on the age
def calc_ticket_price(var_age):

    #Ticket is $7.5 for users under 16
    if var_age < 16:
        price = 7.5

    #Ticket is $10 for users between 16 and 64
    elif var_age < 65:
        price = 10.5

    #Ticket price is $6.50 for seniors (65+)
    else:
        price = 6.5

    return price

# Checks that users enter a valid response
#Cash / credit based on a list of options
def string_checker(question, num_letters, valid_responses):

    error = (f"Please choose {valid_responses[0]} or {valid_responses[1]}")

    if num_letters == 1:
        short_version = 1
    else:
        short_version = 2
    
    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:short_version] or response == item:
                return item
            
        print(error)
        print()


#Main routine

#Set maximum number of tickets below
MAX_TICKETS = 3
tickets_sold = 0

#Lists below
yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

#Ask user if they want to see instructions
want_instructions = string_checker("Do you want to read the instructions (y/n): ",1, yes_no_list)

if want_instructions == "yes" or want_instructions == "y":
    print("Instructions go here")

print()

#Loop to sell tickets
tickets_sold = 0
while tickets_sold < MAX_TICKETS:
    name = not_blank("Enter your name (or 'xxx' to quit)")

    if name == 'xxx':
        break

    age = num_check("What is your age?: ")
    print()
    
    if 12 <= age <= 120:
        pass

    elif age < 12:
        print("Sorry you are too young for this movie")
        continue

    else:
        print("That looks like a typo, please try again")
        continue

    #Calculate ticket cost
    ticket_cost = calc_ticket_price(age)



    tickets_sold += 1
    
#Output number of tickets sold
if tickets_sold == MAX_TICKETS:
    print("Congratulations you have sold all the tickets")

else:
    print(F"You have sold {tickets_sold} ticket/s. There is {MAX_TICKETS - tickets_sold} remaining.")