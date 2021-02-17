

# functions go here
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("<error> Unknown Answer "
                  "Detected. Please Input Yes/No")


def instructions():
    print("***How to Play***")
    print()
    print("The rules go here")
    print()
    return ""


def num_check(question, low, high):
    error = "Please enter a whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))
            # if amount is too low / too high give
            if low < response <= high:
                return response

            # output error
            else:
                print(error)
        except ValueError:
            print(error)


# Main routine goes here...
show_instructions = yes_no("Have you played my "
                           "game before? ")

if show_instructions == "no":
    instructions()

# Ask user how much they want to play with...
print()
how_much = num_check("How much would you "
                     "like to play with? ", 0, 10)
print()
print("You will be spending ${}".format(how_much))
print()

print("program continues")