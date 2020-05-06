# Implement a class to hold room information. This should have name and
# description attributes.

class Room:

    # exits
    n_to = None
    s_to = None
    e_to = None
    w_to = None
    u_to = None
    d_to = None

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
    
    def get_next_room(self, direction):

        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "e":
            return self.e_to
        elif direction == "w":
            return self.w_to
        elif direction == "u":
            return self.u_to
        elif direction == "d":
            return self.d_to

    def print_items(self):

        if len(self.items) > 0:

            print("On the ground, you see the following:")

            item_names = [item.get_name() for item in self.items]
            print(", ".join(item_names))

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):

        # remove item if it exists
        if self.items.index(item) >= 0:
            self.items.remove(item)
        
    def describe(self):
        print(self.name)
        print("  " + self.description)
        self.print_items()        

