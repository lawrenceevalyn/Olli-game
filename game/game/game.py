# import all the other code I wrote

from map import *
from parser import *
from lexicon import *
from inventory import *


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

a_game = GameEngine(entrance)
a_game.play()