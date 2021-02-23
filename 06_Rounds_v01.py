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
    balance -= 1
    print("Balance: ", balance)
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