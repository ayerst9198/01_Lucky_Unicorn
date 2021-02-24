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
            print("I don't understand. "
                  "Stop acting smart and just input Yes or No")


def cont():
    input("Enter anything to continue the Game :D")


def instructions():
    print("***How to Play***")
    print()
    print("Welcome to Lucky Unicorns")
    print()
    print("The aim of the game is to make as much money as possible")
    print()
    print("A random token will be generated from a unicorn, horse, donkey, or zebra:")
    print()
    print("Unicorns are worth $4.")
    print("If you get a Zebra or a Horse, you lose $0.50")
    print("Watch out for Donkeys!")
    print("If you get a Donkey, you lose $1!")
    print()
    print("When you run out of money; YOU LOSE")
    print()
    print("Enjoy!")
    print()
    cont()
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
    elif:

    else:
        play_again = input("Press <Enter> to play again "
                           "or 'xxx' to quit ")

print()
print("Final Balance: ${}".format(balance))