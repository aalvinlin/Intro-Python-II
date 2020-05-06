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
        
    def describe(self):
        print(self.name)
        print("  " + self.description)
