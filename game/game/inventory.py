from map import *
import config
from robot import *

# All the items in the game, and the game's name for them

descriptions = {
    'robot' : "The robot librarian is distressed. It can't shut down. ",
    'door' : "You can see the door to the exit. If only you could go through it. ",
    'pencils' : "a jar of tiny pencils",
    'scanner' : "a barcode scanner",
    'bedtime story' : "a copy of your favourite bedtime story, Goodnight, Moon",
    'fairytales' : "a heavy volume of scary fairytales",
    'rhymes' : "a brightly-coloured book of children's rhymes",
    'encyclopedia' : "a seven-volume encyclopedia of dinosaurs",
    'USB stick' : "a mysterious USB stick",
    'cable' : "a cable to connect a printer to something",
    'mousepads (36)' : "thirty-six mousepads",
    'trash can' : "a half-full trash can",
    'water' : "water. You wonder if you should clean it up",
    'paper towels' : "paper towels",
    'broom' : "a broom",
    'lipstick' : "a half-used tube of lipstick in a fetching shade of coral",
    'lint' : "lint.",
    'library card' : "a library card with a studious photograph of yourself",
    'teddy bear' : "a small toy, kind of like a bear",
    'closet door' : "a door to a small supply closet",
    'testobject' : "This is a drill. Please remain calm. In a real emergency, you will be notified."
    }
    # Because I'm using dicts, these descriptions stick with the items no matter
    # what inventory they're in at the time!

givetext = {
    'pencils' : "You hold out the pencils you just took from the robot's own desk.",
    'testobject' : "You have passed the test!",
    'hug' : "You embrace the robot, and it makes a happy noise.",
    'love' : "The power of love saves the day.",
    'friendship' : "The power of friendship saves the day.",
    'lint' : "You reach deep into your pocket and offer the robot the bit of lint you find there.",
    'teddy bear' : "You hold out the teddy bear. The robot chimes happily in recognition, and reaches out for it."
    'bedtime story' : "You hold out the book with the bedtime story, but the robot just looks at it sadly. Maybe you should read it to them?"
    }

    
# Initial distribution of items in various inventories

items = { # inv names need to be room name + _inv (see map for room names)
    'entrance_inv' : ['robot', 'door', 'pencils', 'scanner'],
    'stacks_inv' : ['bedtime story', 'fairytales', 'rhymes', 'encyclopedia', 'teddy bear'],
    'lab_inv' : ['USB stick', 'cable', 'mousepads (36)', 'trash can'],
    'bathroom_inv' : ['water', 'lipstick'],
    'player_inv' : ['lint', 'library card'],
    'closet_inv' : ['closet item', 'broom', 'paper towels'],
    'robot_inv' : [],
    'the_void' : ['love', 'friendship'] # this is so I can make water go away
    # also a place to store intangibles that the player can nonetheless give
    }

winningitems = {'teddy bear', 'love', 'friendship', 'testobject'}

# Looking at items

def printinv(inv):
    for i in items[inv]:
        print descriptions[i]


# Functions to do stuff with the items

def move(dict, item, inv_from, inv_to):
    # will move the item between the lists in the items dict
    dict[inv_from].remove(item)
    dict[inv_to].append(item)

def takeobj(room, obj_taking):
    inv_from = room.name + "_inv"
    print "taking " + obj_taking + " from " + inv_from
    
    # make sure that is a thing they can take
    if obj_taking not in items[inv_from]:
        # if it's not takable, print an error
        print "You can't take that."
                
    else: # if it's all good, put that thing in their inventory!
        move(items, obj_taking, inv_from, 'player_inv')
        print "You now have:"
        printinv('player_inv')
             
    return room


def dropobj(room, obj_dropping):
    inv_to = room.name + "_inv"
    print "dropping " + obj_dropping + " into " + inv_to
            
    # make sure that is a thing they can drop
    if obj_dropping not in items['player_inv']:
        # if it's not droppable, print an error
        print "You have to have something before you can drop it."
        
    else: # if it's all good, put that thing in their inventory!
        move(items, obj_dropping, 'player_inv', inv_to)
        print "Player inventory now contains: "
        for i in items['player_inv']:
            print descriptions[i]
    
    return room


def useobj(room, obj_using): # right now can only use paper towels, but this is
                             # gonna be a complicated one!

# use paper towels

    # if they're not trying to use the towel, call the whole thing off
    if obj_using not in ('paper towels', 'bedtime story'):
        print "You don't have a use for " + obj_using
    # later when there are more usable items, replace this with a list
    # of usable items & check against the list
            
    # if they are using the towel, make sure there's water around to use on
    else:
        # time to proceed with using the items!
        
        # paper towel track
        if obj_using == 'paper towels':
            if room != bathroom: # make sure they're in the bathroom
                print "There's no use for paper towels in this room."
        
            else: # then make sure the bathroom is wet
                if 'water' not in items['bathroom_inv']:
                    print "The bathroom is already clean!"
            
                else: # if it's all good, do some cleaning!
                    print "Using paper towels in the bathroom..."
                    # move water and paper towels to the void
                    move(items, 'water', 'bathroom_inv', 'the_void')
                    print "The bathroom is clean!"
                    move(items, 'paper towels', 'player_inv', 'the_void')
                    print "You throw away the soggy paper towels."
        
        elif obj_using == 'bedtime story':
            # check that the robot is ready for  a sory
            if robot_status != 'wantsstory':
                print "The robot doesn't seem able to focus on the story."
                print "Maybe it needs something to calm down first?"
            
            # read to the robot
            else:
                print "You read the bedtime story to the robot."
                print "Its lights slowly dim as it relaxes into the story."
                print "Finally, the robot goes to sleep."
            
            # you win!
            
        else:
            print "This should never happen."
    
    return room                    # why do I always return this? do I have to?


def giveobj(room, obj_giving):
    # check that they are in the same room as the robot
    if room != entrance:
        print "There's nobody here to give that to."
    
    else:
        # check that the item is givable
        if obj_giving in items['player_inv'] or items['the_void']:
            print "This is a givable item."
            
            # figure out where it is cuz we'll need to know later
            if obj_giving in items['player_inv']:
                print "You have this item."
                gift_inv = 'player_inv'
            
            elif obj_giving in items['the_void']:
                print "This item is intangible."
                gift_inv = 'the_void'
            
            else:
                print "This should never happen."
            
            if obj_giving in givetext:
                print givetext[obj_giving]
            else:
                pass
            
            # check what happens next to the item
            if obj_giving not in winningitems:
                print "The robot rejects your gift."
            
            else:
                print "This is a comforting item!"
                print "Moving " + obj_giving + " from " + gift_inv
                
                # give the item to the robot
                move(items, obj_giving, gift_inv, 'robot_inv')
                
                print "The robot seems much calmer now."
                print "Maybe it is ready to shut down?"
                # once the robot has gotten one comfort item, it is ready
                updaterobot("wantsstory")         # for its bedtime story
            
            if obj_giving in givetext:
                print givetext[obj_giving]
            else:
                pass
        
        else:
            print "You can't give what you don't have!"
        
            
    return room