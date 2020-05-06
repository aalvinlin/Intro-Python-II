from item import LightSource

class Room:

    # exits
    n_to = None
    s_to = None
    e_to = None
    w_to = None
    u_to = None
    d_to = None

    def __init__(self, name, description, is_light=False):
        self.name = name
        self.description = description
        self.items = []
        self.is_light = is_light

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

    # return the Item object with the specified name if it exists
    def get_item_by_name(self, item_name):
        requested_item = [item for item in self.items if item.get_name() == item_name]

        if len(requested_item) == 1:
            return requested_item[0]
        else:
            return None

    # add an Item object to the room
    def add_item(self, item):
        self.items.append(item)

    # remove a requested Item object from the room
    def remove_item(self, item):
        # remove item if it exists
        if item:
            self.items.remove(item)
    
    # get a list of all Item objects in the room
    def return_items_in_room(self):
        return self.items

    def describe(self, player_illumination_status):

        print(self.name)

        # display description and items only if it is light enough to see them
        if self.is_illuminated() or player_illumination_status:
            
            print("  " + self.description)
            self.print_items()

        else:
            print("It's too dark to see anything here.")
    
    # determine if there is enough light to see in the room
    def is_illuminated(self):

        # check for a light source object
        light_sources = [item for item in self.items if isinstance(item, LightSource)]

        # return true if naturally lit or light source found
        return self.is_light or len(light_sources) > 0

