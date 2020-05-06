# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:

    inventory = []

    def __init__(self, starting_room, name):
        self.current_room = starting_room
        self.name = name

    def get_location(self):
        return self.current_room

    def move_to_location(self, next_room):
        self.current_room = next_room

    def drop_item(self, item):

        # remove item if it exists
        if self.inventory.index(item) >= 0:
            self.inventory.remove(item)
        
        else:
            print("You don't have this in your inventory!")
