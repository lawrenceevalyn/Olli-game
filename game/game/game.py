# import all the other code I wrote

from map import *
from parser import *
from parser import parse_input # still feels weird that I have to say this one
from lexicon import *          # by name seperately, but c'est la vie
from inventory import *


# this is what will run the game

def play(first_room):
      current_room = first_room
      
      while current_room != exit:
        # the basic premise is that the player is always in a room,
        # always sees the shortdesc of that room,
        # and always sees a prompt for their next action
        print current_room.shortdesc
        player_input = raw_input("> ")
            
        # need an easy out to end the game
        if player_input in ["Q", "q"]:
            print "Goodbye"
            current_room = exit
        else:
            curent_room = parse_input(player_input, current_room)
            # don't have to print anything, bc parser prints
            # "output" of parse_input needs to be a room
            # (the player may not move rooms, based on the input, but the game
            # engine still needs to know explicitly they're in the same place)


# hey! let's run the game now!

print "Welcome to the game!"
play(entrance)