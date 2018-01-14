# define how rooms work

class Room(object):

    def __init__(self, name, shortdesc, longdesc):
        self.name = name
        self.shortdesc = shortdesc
        self.longdesc = longdesc
        self.paths = {} # an empty dict

    def go(self, direction): # direction will be passed in, N S E W
        return self.paths.get(direction, "invalid path")
        # get() is a standard python method, returns a value for the given key
        # the second thing specified is what it returns if there's nothing there

    def add_paths(self, paths): # defines a way to add to the paths dict
        self.paths.update(paths)


# create all the rooms

entrance = Room("entrance", "You are at the front desk.", "Longer description appears when you look at the entrance.")
exit = Room("exit", "never see shortdesc", "never see longdesc")
stacks = Room("stacks", "You are in the stacks, near the children's literature.", "Longer description appears when you look at the stacks.")
lab = Room("lab", "You are in the computer lab.", "Longer description appears when you look at the lab.")
bathroom = Room("bathroom", "You are in the bathroom.", "Longer description appears when you look at the bathroom.")
closet = Room("closet", "You are in a small supply closet.", "Longer description appears when you look at the closet.")


# add all the paths between the rooms (fill up their dicts)
# (make sure paths are reciprocated if they are meant to go both ways)

entrance.add_paths({'north': exit, 'south': stacks, 'east': lab, 'west': bathroom})
exit.add_paths({'south': entrance})
stacks.add_paths({'north': entrance})
lab.add_paths({'west': entrance, 'north':closet})
bathroom.add_paths({'east': entrance})
closet.add_paths({'south':lab})

# a function to look at those paths

def listpaths(room):
    print "Exits are: " + ', '.join([k for k in room.paths.keys()])
    # this prints all the keys for the room's "paths" dict
    # as per https://stackoverflow.com/questions/24328208/concise-way-to-print-dictionary-keys-in-a-nice-format
        


# let the player move between rooms

def travelto(room, destination):
    # destination will be passed in as the key to the paths dict
    next_room = room.go(destination) # "go" is defined in Room class above
    
    if next_room == "invalid path":
        print "You can't go that way."
        room = room
    else:
        room = next_room
    
    return room