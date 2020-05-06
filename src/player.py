# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:

    inventory = []

    def __init__(self):
        self.room = 'outside'

    def get_location(self):
        return self.room

    def move_to_location(self, new_room):

        pass
        # if new_room.get_next_room(direction)

        # self.room = new_room

    def drop_item(self, item):

        # remove item if it exists
        if self.inventory.index(item) >= 0:
            self.inventory.remove(item)
        
        else:
            print("You don't have this in your inventory!")
