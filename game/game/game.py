# import all the other code I wrote

from map import *
from parser import *
from lexicon import *
from inventory import *


# this is what will run the game

class GameEngine(object):

    # set up the things the game engine will need
    def __init__(self, current_room):
        self.current_room = current_room
    
    # define what the game engine does once a game begins
    def play(self):
        while self.current_room != exit:
            # the basic premise is that the player is always in a room
            # and always sees a prompt
            player_input = raw_input("> ")
            
            # essentially, this is where I want to pass off the player's input
            # to the parser; everything after this really belongs in the parser.
            # parse(player_input)
            # parser does NOT have to make sure to return anything in particular
            # because as long as the room is not the exit, the prompt will
            # always appear for a new input!! :D
            
            # the player has a couple options of actions within a room!
            if player_input == "Q":
                print "Goodbye"
                self.current_room = exit
            
            elif player_input == "look":
                print self.current_room.longdesc
                
            # player can go to different rooms
            elif player_input == 'north' or 'south' or 'east' or 'west' :
                if self.current_room.go(player_input) == None:
                    print "You can't go that way."
                else:
                    self.next_room = self.current_room.go(player_input)
                    print self.next_room.name
                    print self.next_room.shortdesc
                    self.current_room = self.next_room
                    
            # player can look at things in the room
            
            # player can pick up / put down items

a_game = GameEngine(entrance)

# let's run the game now!

print "Welcome to the game!"
a_game.play()