show_instructions = ""
while show_instructions.lower() != "xxx":
    # Ask user if they have played before
    show_instructions = input("Have you played my game before? ").lower()
    # If yes - output 'program continues'
    if show_instructions == "yes" or show_instructions == "y":
        print("program continues")
    elif show_instructions == "no" or show_instructions == "n":
        print("Display Instructions")
    # If no - output 'display instructions'
    else:
        print("<error> Unknown Answer Detected. Please Input Yes/No")