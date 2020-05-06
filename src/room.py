# Implement a class to hold room information. This should have name and
# description attributes.

class Room:

    exits = {
        "n": None,
        "s": None,
        "e": None,
        "w": None,
        "u": None,
        "d": None
    }

    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def n_to(self):
        return exits['n']
    
    def s_to(self):
        return exits['s']
    
    def e_to(self):
        return exits['e']
    
    def w_to(self):
        return exits['w']
    
    def u_to(self):
        return exits['u']
    
    def d_to(self):
        return exits['d']
    
    def describe(self):
        print(self.name)
        print("  " + self.description)
