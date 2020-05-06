class Item:

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def on_take(self):
        print("You picked up the " + self.name + ".")
        print("  " + self.description + "\n")

    def on_drop(self):
        print("You dropped your " + self.name + ".")

class LightSource(Item):

    def __init__(self, name, description):
        super().__init__(name, description)
    
    def on_drop(self):
        print("It's not wise to drop your source of light!\nYou dropped your " + self.name + ".")
