from sys import exit

# define how rooms work

class Room(object):

    def __init__(self, name, shortdesc, longdesc):
        self.name = name
        self.shortdesc = shortdesc
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)


# create all the rooms

entrance = Room("Entrance", "You are at the front desk.")
exit = Room("Exit", "You have left the library! Congratulations!")
stacks = Room("Stacks", "You are in the stacks, near the children's literature.")
lab = Room("ComputerLab", "You are in the computer lab.")
bathroom = Room("Bathroom", "You are in the bathroom.")
closet = Room("Supply Closet", "You are in a small supply closet.")
    

# add all the paths between the rooms
# (make sure paths are reciprocated if they are meant to go both ways)

entrance.add_paths({'north': exit, 'south': stacks, 'east': lab, 'west': bathroom})
exit.add_paths({'south': entrance})
stacks.add_paths({'north': entrance})
lab.add_paths({'west': entrance, 'north':closet})
bathroom.add_paths({'east': entrance})
closet.add_paths({'south':lab})