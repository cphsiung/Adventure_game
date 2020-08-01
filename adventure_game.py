import time
import random

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(0)

def intro(items, enemy):
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {enemy} is somewhere around here, "
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective),"
                " dagger.")

def where_to_go(items, enemy):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    choice = input("What would you like to do?\n"
                   "(Please enter 1 or 2).\n")
    if choice == "1":
        knock_door(items, enemy)
    elif choice == "2":
        cave(items, enemy)
    else:
        print_pause("Please enter 1 or 2.")
        where_to_go(items, enemy)

def knock_door(items, enemy):
    print_pause(f"You knock on the door and out steps a {enemy}.")
    print_pause(f"The {enemy} attacks you!")
    fight_or_flight(items, enemy)

def cave(items, enemy):
    if "Legendary Sword" in items:
        print_pause("You've been here before and there's nothing else "
                    "to do here.")
        print_pause("You walk back out to the field")
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the Legendary Sword!")
        print_pause("You took the Legendary Sword and walk back to the field.")
        items.append("Legendary Sword")
    where_to_go(items, enemy)

def fight_or_flight(items, enemy):
    fight = input("Would you like to (1) fight or (2) run away?\n")
    if fight == "1":
        if "Legendary Sword" in items:
            print_pause(f"As the {enemy} moves to attack, "
                        "you unsheath your new Legendary Sword.")
            print_pause(f"The {enemy} takes one look at your shiny new toy "
                        "and runs away!")
        else:
            print_pause(f"The {enemy} is too strong.")
            print_pause("You're defeated...")
    elif fight == "2":
        print_pause("You run away!")
    else:
        print_pause("Only enter 1 or 2")
        fight_or_flight(items, enemy)

def play_again():
    again = input("Would you like to restart? y/n \n").lower()
    if again == "y":
        play_game()
    elif again == "n":
        print_pause("Thank you for playing.")
    else:
        print_pause("Only enter y/n")
        play_again()

def play_game():
    items = []
    enemy = random.choice(["pirate", "wicked fairie", "dragon"])
    intro(items, enemy)
    where_to_go(items, enemy)
    play_again()

play_game()
