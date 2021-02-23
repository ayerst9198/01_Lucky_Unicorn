import random


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
balance = how_much

rounds_played = 0

play_again = input("Please press <Enter> to play... ").lower()
while play_again == "":

    # increase # of rounds played
    rounds_played += 1

    # print round number
    print()
    print("*** Round #{} ***".format(rounds_played))
    chosen_num = random.randint(1, 100)

    # Adjust balance
    # if the random # is between 1 and 5,
    # user gets a unicorn (add $4 to the balance)
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4
    # if the random # is between 6 and 36,
    # user gets a donkey (subtract $1 from balance)
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        balance -= 1
    # token is either horse or zebra...
    # either way subtract $0.5 from balance
    else:
        # if the number is even, set the chosen
        # item to horse
        if chosen_num % 2 == 0:
            chosen = "horse"
        # if the number is odd, set the chosen
        # item to zebra
        else:
            chosen = "zebra"
        balance -= 0.5

    print("You got a {}. Your balance is "
          "${:.2f}".format(chosen, balance))
    print()

    if balance < 1:
        play_again = "xxx"
        print("Sincere apologies kind sir,"
              " but you are stone broke. "
              "Come back when you can afford it :D")
    else:
        play_again = input("Press <Enter> to play again "
                           "or 'xxx' to quit ")

print()
print("Final Balance: ", balance)