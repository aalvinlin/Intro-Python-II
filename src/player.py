# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:

    self.inventory = []

    def __init__(self):
        self.room = 'outside'
    
    def drop_item(item):

        # remove item if it exists
        if self.inventory.index(item) >= 0:
            self.inventory.remove(item)
        
        else
            print("You don't have this in your inventory!")
