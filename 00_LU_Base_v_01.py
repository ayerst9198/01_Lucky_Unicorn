

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


# Main routine goes here...
show_instructions = yes_no("Have you played my "
                           "game before? ")

if show_instructions == "no":
    instructions()

print("program continues")