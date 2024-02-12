#Function goes here
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
while True:
    name = not_blank("Enter your name (or 'xxx' to quit)")
    if name == "xxx":
        break

print("we are done")