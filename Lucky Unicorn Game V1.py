
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


# Main routine goes here...
show_instructions = yes_no("Have you played my "
                           "game before? ")
print("You chose {}".format(show_instructions))
print()
# Ask user if they have played before
having_fun = input("Did you enjoy my ULTRA MEGA AWESOME UNBEATABLE GAME?").lower()
# If yes - output 'program continues'
if having_fun == "yes" or having_fun == "y":
    print("Yay.")


# If no - output 'display instructions'
elif having_fun == "no" or having_fun == "n":
    print()
    print("Oh...")
# If invalid - output '<error>'

else:
    print()
    print("That's not what I asked :/")