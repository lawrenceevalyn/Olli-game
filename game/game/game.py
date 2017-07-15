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
        # the basic premise is that the player is always in a room
        # and always sees a prompt for their next action
        print current_room.shortdesc
        player_input = raw_input("> ")
            
        # need an easy out to end the game
        if player_input in ["Q", "q"]:
            print "Goodbye"
            current_room = exit
        else:
            parse_input(player_input) # don't print, bc parser prints
                                       # (output won't get returned to here)
            
            # parser does NOT have to make sure to return anything in particular
            # because as long as the room is not the exit, the prompt will
            # always appear for a new input!! :D
            
            
            #elif player_input == "look":
            #    print self.current_room.longdesc
            #    
            # player can go to different rooms
            #elif player_input == 'north' or 'south' or 'east' or 'west' :
            #    if self.current_room.go(player_input) == None:
            #        print "You can't go that way."
            #    else:
            #        self.next_room = self.current_room.go(player_input)
            #        print self.next_room.name
            #        print self.next_room.shortdesc
            #        self.current_room = self.next_room

# let's run the game now!

print "Welcome to the game!"
play(entrance)