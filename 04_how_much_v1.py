# Functions go here


# Main routine goes here

error = "Please enter a whole number between 1 and 10"

valid = False
while not valid:
    # ask the question
    response = int(input("How much would you "
                         "like to play with? "))
    # if amount is too low / too high give
    if 0 < response <= 10:
        print("you have asked to play "
              "with ${}".format(response))

    # output error
    else:
        print(error)