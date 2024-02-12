#Functions go here

#Checks if user has entered yes / no to a question
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        
        elif response == "no" or response == "n":
            return "no"
        
        else:
            print("Please answer yes or no")

#Checks that user response is not blank
def not_blank(question):
    while True:
        response = input(question)

        #If response is blank output error
        if response == "":
            print("Sorry this can't be blank. Please try again")

        else:
            return response
        
#Main routine

#Set maximum number of tickets below
MAX_TICKETS = 3
tickets_sold = 0

#Ask user if they want to see instructions
want_instructions = yes_no("Do you want to read the instructions? ").lower()

if want_instructions == "yes" or want_instructions == "y":
    print("Instructions go here")

print()

#Loop to sell tickets
tickets_sold = 0
while tickets_sold < MAX_TICKETS:
    name = not_blank("Enter your name (or 'xxx' to quit)")

    if name == 'xxx':
        break

    tickets_sold += 1
    
#Output number of tickets sold
if tickets_sold == MAX_TICKETS:
    print("Congratulations you have sold all the tickets")

else:
    print(F"You have sold {tickets_sold} ticket/s. There is {MAX_TICKETS - tickets_sold} remaining.")