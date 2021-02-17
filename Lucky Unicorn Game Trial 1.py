show_instructions = ""
while show_instructions.lower() != "xxx":
    # Ask user if they have played before
    show_instructions = input("Have you played my game before? ").lower()
    # If yes - output 'program continues'
    if show_instructions == "yes" or show_instructions == "y" or show_instructions == "Yes" \
            or show_instructions == "Y" or show_instructions == "YEs" \
            or show_instructions == "YES" or show_instructions == "YeS" \
            or show_instructions == "yES" or show_instructions == "yeS":
        print("program continues")
    elif show_instructions == "no" or show_instructions == "n" \
        or show_instructions == "nO" or show_instructions == "N" \
        or show_instructions == "No" or show_instructions == "nO":
        print("Display Instructions")
    # If no - output 'display instructions'
    else:
        print("<error> Unknown Answer Detected. Please Input Yes/No")
# Trial was pointless. the .lower() command deemed my hard work pointless. I leave this room a broken man.