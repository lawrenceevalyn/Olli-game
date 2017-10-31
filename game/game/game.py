# import all the other code I wrote

from map import *
from parser import *
from parser import parse_input # still feels weird that I have to say this one
from lexicon import *          # by name seperately, but c'est la vie
from inventory import *
from robot import *
import config


# this is what will run the game

def play(first_room):
    current_room = first_room
    
    while current_room != exit:
    # the basic premise is that the player is always in a room,
    # always sees some info about that room,
    # and always sees a prompt for their next action
    
        # show some info:
        print current_room.shortdesc
        listpaths(current_room)
        print "Robot status: " + config.robot_status
        
        # prompt response:
        player_input = raw_input("> ")
            
        # need an easy out to end the game
        if player_input in ["Q", "q", "quit"]:
            print "Goodbye"
            current_room = exit
        
        else:
            next_room = parse_input(player_input, current_room)
            current_room = next_room
            # don't have to print anything, bc parser prints
            # "output" of parse_input needs to be a room
            # (the player may not move rooms, based on the input, but the game
            # engine still needs to know explicitly they're in the same place)


# hey! let's run the game now!

print "Welcome to the game!"
play(entrance)