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

    # directions
    directions = {
        "n": n_to,
        "s": s_to,
        "e": e_to,
        "w": w_to,
        "u": u_to,
        "d": d_to
    }

    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def get_next_room(self, direction):
        return self.directions[direction]

    def describe(self):
        print(self.name)
        print("  " + self.description)
