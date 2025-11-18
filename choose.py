import time
import random  # Import the random module
# Function to greet the user
def greet():
    print("Hello, adventurer! Welcome to the land of Python.")
    time.sleep(1)
    name = input("What is your name? ")
    print(f"Nice to meet you, {name}!")
    time.sleep(1)
    return name
# Function for the adventure choice
def choose_path():
    print("\nYou find yourself at a crossroads. Where will you go?")
    print("1. Enter the dark forest.")
    print("2. Walk along the beach.")
    choice = input("Enter 1 or 2: ")
    time.sleep(1)
    # Conditional
    if choice == "1":
        forest_path()
    elif choice == "2":
        beach_path()
    else:
        print("That's not a valid option!")
        time.sleep(1)
        home()
def home():
    print("You arrive home safely, but you still want to do something.")
    time.sleep(.5)
    print("You decide to go through all of this all over again.")
    print("1. Enter the dark forest.")
    print("2. Walk along the beach.")
    choice2 = input("Enter 1 or 2: ")
    if choice2 == "1":
        forest_path()
    elif choice2 == "2":
        beach_path()
    else:
        print("That's not a valid option!")
        time.sleep(1)
        home()
# Function for forest path
def forest_path():
    print("\nYou enter the dark forest. It's spooky and quiet.")
    time.sleep(2)
    print("Suddenly, you hear a noise behind you!")
    time.sleep(2)
    print("Do you want to run or stay and see what it is?")
    action = input("Type 'run' or 'stay': ")
    # Conditional with random event
    if action == "run":
        outcome = random.choice(["You trip over a root but manage to get up and run away.", 
                                 "You run as fast as you can and escape safely.",
                                 "You run as fast as you can, but you don’t see the giant hole, and you fall in."])
        print(outcome)
        if outcome == "You run as fast as you can, but you don’t see the giant hole, and you fall in.":
            print("You are unharmed from the fall.  You yell out for help, but no one comes.")
        else:
            print("You make your way back home and have a cup of tea.")
    elif action == "stay":
        	encounter = random.choice(["A friendly rabbit appears! It guides you out safely.", 
                                   "A shadowy figure appears... but it turns out to be just a deer."])
        	print(encounter)
    else:
        	print("That's not a valid action, but nothing happens. You walk back safely.")

# Function for beach path
def beach_path():
    print("\nYou walk along the beach. The waves are calming.")
    time.sleep(2)
    print("You see a shiny object in the sand. Do you want to pick it up?")
    action = input("Type 'yes' or 'no': ")

    if action == "yes":
        treasure = random.choice(["You pick up the shiny object and discover it's a golden coin!", 
                                  "It's a piece of glass, but it's smooth and pretty."])
        print(treasure)
    elif action == "no":
        print("You walk past the object, but feel relaxed by the sound of the waves.")
    else:
        print("You hesitate, but nothing happens. You continue walking.")

# Main program starts here
def start_adventure():
    name = greet()
    print(f"{name}, your adventure begins now!")
    time.sleep(1)
    choose_path()

start_adventure()


