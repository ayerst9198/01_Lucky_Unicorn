import random


# set balance for testing purposes
balance = 5

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