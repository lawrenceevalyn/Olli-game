from sys import exit

# define how rooms work

class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
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
    

# add all the paths between the rooms
# (make sure paths are reciprocated if they are meant to go both ways)

entrance.add_paths({'north': exit, 'south': stacks, 'east': lab, 'west': bathroom})
exit.add_paths({'south': entrance})
stacks.add_paths({'north': entrance})
lab.add_paths({'west': entrance})
bathroom.add_paths({'east': entrance})



# this is what will run the game

class GameEngine(object):

    def __init__(self, current_room):
        self.current_room = current_room
    
    def play(self):
        while self.current_room != exit:
            print self.current_room.description
        
            player_input = raw_input("> ")
            
            if player_input == "Q":
                print "Goodbye"
                self.current_room = exit
            
            elif player_input == 'north' or 'south' or 'east' or 'west' :
                if self.current_room.go(player_input) == None:
                    print "You can't go that way."
                else:
                    self.next_room = self.current_room.go(player_input)
                    print self.next_room.name
                    self.current_room = self.next_room
        
        print self.current_room.description


# let's run the game now!

#a_game = GameEngine(entrance)
# a_game.play()

# just kidding, the browser will run the game