# Fox, chicken, grain program
# https://time2code.today/python-course/python-fox-chicken-grain

# Initial value
farmer = False
fox = False
chicken = False
grain = False

def win():
    if farmer and fox and chicken and grain:
        print("You win!")
        return True

def lose():
    if fox == chicken != farmer:
        print("The fox ate the chicken.")
        return True
    if chicken == grain != farmer:
        print("The chicken ate the grain.")
        return True
    return False

def status():
    print("-----------------------")
    print("This side of the river:")
    if not farmer:
        print("Farmer")
    if not fox: 
        print("Fox")
    if not chicken:
        print("Chicken")
    if not grain:
        print("Grain")
    print("\nOther side of the river:")
    if farmer:
        print("Farmer")
    if fox: 
        print("Fox")
    if chicken:
        print("Chicken")
    if grain:
        print("Grain")
    print("-----------------------")

# Main loop
while not win() and not lose():
    status()
    # User input handling
    while True:
        try:
            choice = int(input("\nWhich item will you take in your rowboat to the other side?\n[1] Farmer\n[2] Fox\n[3] Chicken\n[4] Grain\nEnter: "))
            if 1 <= choice <= 4: #Valid range check
                break
            else:
                print("Invalid input. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
    # Logic operation
    match choice:
        case 1:
            farmer = not farmer
        case 2:
            if farmer == fox:
                farmer = not farmer
                fox = not fox
            else:
                print("Fox and farmer in different side")
        case 3:
            if farmer == chicken:
                farmer = not farmer
                chicken = not chicken
            else:
                print("Chicken and farmer in different side")
        case 4:
            if farmer == grain:
                farmer = not farmer
                grain = not grain
            else:
                print("Grain and farmer in different side")
        case _: #Nothing
            print("Input invalid")
