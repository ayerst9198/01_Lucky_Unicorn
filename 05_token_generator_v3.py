import random

# main routine goes here

STARTING_BALANCE = 100

balance = STARTING_BALANCE
# testing loop to generate 2 0 tokens
for item in range(0,10):
    chosen_num = random.randint(1,100)

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
print()
print("Starting Balance = ${}".format(STARTING_BALANCE))
print("Final Balance = ${}".format(balance))
print()