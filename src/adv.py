from data import room
from room import Room
from player import Player
from item import Item

#
# Main
#

def show_instructions():
    print("To move, type 'n', 's', 'e', or 'w'.")
    print("To quit, type 'q'.")
    print("To pick up an item, type 'get (item name)' or 'take (item name)'.")
    print("To drop an item, type 'drop (item name).")
    print("To view your inventory, type 'i'.")
    print("To view these instructions again, type 'h'.")

print("Welcome to Adventure Game #1")
show_instructions()

direction_abbreviations = {
    "n": "north",
    "s": "south",
    "e": "east",
    "w": "west",
    "u": "up",
    "d": "down"
}

direction_adj_phrase = {
    "n": "to the north",
    "s": "to the south",
    "e": "to the east",
    "w": "to the west",
    "u": "above",
    "d": "below"
}

# Make a new player object that is currently in the 'outside' room.

player = Player(room['outside'], "Adventurer #215")

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:

    # get player's current room and print its description
    current_room = player.get_location()
    current_room.describe()
    
    # prompt for user input
    user_input = input("> ").lower()

    # get all words separated by spaces
    input_words = user_input.strip().split(" ")

    # single-word actions
    if len(input_words) == 1:

        if (user_input == 'q'):
            break

        elif (user_input == 'h'):
            show_instructions()

        elif (user_input in ['i' , 'inventory']):
            player.show_inventory()

        elif (user_input in direction_abbreviations):

            # check if current room has an exit in the requested direction
            next_room = current_room.get_next_room(user_input)

            if next_room:
                # move user to new room
                player.move_to_location(next_room)
                print("You move " + direction_abbreviations[user_input] + ".")
            else:
                print("There is no exit " + direction_adj_phrase[user_input] + " from here.")
    
    # two-word actions
    elif len(input_words) == 2:

        verb = input_words[0]
        direct_object = input_words[1]

        if (verb in ['get', 'take']):
            player.get_item(direct_object)
        
        elif (verb == 'drop'):
            player.drop_item(direct_object)

    # print an extra line at the end to separate actions
    print("")
