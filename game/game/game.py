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
            # and always sees the description of that room plus a prompt
            print self.current_room.shortdesc
            player_input = raw_input("> ")
            
            # the player has a couple options of actions within a room!
            if player_input == "Q":
                print "Goodbye"
                self.current_room = exit
            
            #player can go to different rooms
            elif player_input == 'north' or 'south' or 'east' or 'west' :
                if self.current_room.go(player_input) == None:
                    print "You can't go that way."
                else:
                    self.next_room = self.current_room.go(player_input)
                    print self.next_room.name
                    self.current_room = self.next_room
            
            # player can pick up / put down items
        
        print self.current_room.shortdesc


# let's run the game now!

a_game = GameEngine(entrance)
a_game.play()