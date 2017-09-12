from sys import exit

# define how rooms work

class Room(object):

    def __init__(self, name, shortdesc, longdesc):
        self.name = name
        self.shortdesc = shortdesc
        self.longdesc = longdesc
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, "invalid path")
        # get() is a standard python method, returns a value for the given key
        # the second thing specified is what it returns if there's nothing there

    def add_paths(self, paths):
        self.paths.update(paths)


# create all the rooms

entrance = Room("entrance", "You are at the front desk.", "Longer description appears when you look at the entrance.")
exit = Room("exit", "You have left the library!", "Congratulations!")
stacks = Room("stacks", "You are in the stacks, near the children's literature.", "Longer description appears when you look at the stacks.")
lab = Room("lab", "You are in the computer lab.", "Longer description appears when you look at the lab.")
bathroom = Room("bathroom", "You are in the bathroom.", "Longer description appears when you look at the bathroom.")
closet = Room("closet", "You are in a small supply closet.", "Longer description appears you look at the closet.")


# add all the paths between the rooms
# (make sure paths are reciprocated if they are meant to go both ways)

entrance.add_paths({'north': exit, 'south': stacks, 'east': lab, 'west': bathroom})
exit.add_paths({'south': entrance})
stacks.add_paths({'north': entrance})
lab.add_paths({'west': entrance, 'north':closet})
bathroom.add_paths({'east': entrance})
closet.add_paths({'south':lab})


# let the player move between rooms

def travelto(room, destination):
        print "running travelto..."
        next_room = room.go(destination)
        
        if next_room == "invalid path":
            print "You can't go that way"
            print "Room is still " + room.name
            room = room
            print "room in travelto is: " + room.name
        else:
            print "next_room is: " + next_room.name
            room = next_room
            print "room in travelto is: " + room.name
        
        return room