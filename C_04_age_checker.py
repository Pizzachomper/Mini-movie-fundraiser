# Functions go here

# Checks users enter an integer to a given question
def num_check(question):
    while True:
        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter an integer")
            print()


# Main routine
tickets_sold = 0

while True:
    name = input("Enter your name / xxx to quit: ")

    if name == "xxx":
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

    tickets_sold += 1
