from lexicon import *
from map import *
from inventory import *

class ParserError(Exception): # I guess this is here so that if there are errors
    pass                      # later, they display the error messages I wrote?

# First there are a lot of functions that turn the input into sentences
# (Doesn't have to call the lexicon directly, because the lexicon was already
# used to give each word its part-of-speech buddy)

# Sentences have the attributes subject, verb, object    # do I need to add
# (NOT subj, verb, obj!)                                 # indirect objects???
class Sentence(object):

    def __init__(self, verb, obj, ind): #subj
        #  we take ('noun', 'robot') tuples of subj etc & get the second word
#        self.subject = subj[1] # i.e., the subject will be 'robot'
        self.verb = verb[1]    # (except it won't because subj is always player)
        self.object = obj[1]
        self.indirectobj = ind[1]

def peek(word_list): # I don't totally understand this function
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None

def match(word_list, expecting): # I almost understand this function?
    if word_list: # this checks that the list isn't empty
        word = word_list.pop(0)  # I think because this "pops" it removes the
                                 # word after it's been parsed? so that as long
        if word[0] == expecting: # as parse_sentence parses subj before obj,
            return word          # it is safe to just grab the next noun
        else:
            return None
    else:
        return None

def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)

def parse_verb(word_list):
    skip(word_list, 'stop')
    
    if peek(word_list) == 'verb':
        return match(word_list, 'verb') # aha! this is where the match function
    else:                               # gets used! it makes sure each word
        raise ParserError("Expected a verb next.")   # only gets parsed once

def parse_object(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)
    
    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        return ('noun', 'implied object')

def parse_indobject(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)
    
    print "next word is "
    print next_word
    
    if next_word == 'noun':
        return match(word_list, 'noun')
    else:
        return ('noun', 'implied indirect object')

#def parse_subject(word_list):          # why would the subject ever be anything
#    skip(word_list, 'stop')            # but the player?
#    next_word = peek(word_list)        # why did I implement this???
#    
#    if next_word == 'noun':
#        return match(word_list, 'noun')
#    elif next_word == 'verb':
#        return ('noun', 'player')
#    else:
#        return ParserError("Expected a verb next.")

def parse_sentence(word_list):
#    subj = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)
    ind = parse_indobject(word_list)
    
    return Sentence(verb, obj, ind) #subj

# this list defines the "shortcut" commands that can skip the parsing process
shortcuts_list = ('n', 'e', 's', 'w', 'l', 'x', 'i', 'N', 'E', 'S', 'W', 'L', 'X', 'I')

def parse_shortcuts(shortcut, room):

    # parse looking shortcuts
    if shortcut in ["l", "L", "x", "X"]:
        print room.longdesc
        output = room

    # parse direction shortcuts
    else:
        if shortcut in ["N", "n"]:   # instead of trying to parse implied "go"
            destination = 'north'    # verbs and make these directions the
        if shortcut in ["E", "e"]:   # objects of sentences, just skip straight
            destination = 'east'     # to parsing them as move commands
        if shortcut in ["S", "s"]:
            destination = 'south'
        if shortcut in ["W", "w"]:
            destination = 'west'
        
        room = travelto(room, destination) # travelto is defined in map.py
        output = room
    
    return output # don't need to print output here, since this function only
                  # runs when parse_input calls it, and parse_input will print


# After all of that sentence business, now we can parse the intended action!!
def parse_input(input, room):
    
    room = room # apparently I have to say this so that anything works later
    
    # compare the input to a list of shortcuts; use shortcut parser if relevant
    if input in shortcuts_list:
        room = parse_shortcuts(input, room)
        output = room
    
    else: # if it's not a shortcut, gotta actually parse it
        
        # input will begin as just a string, e.g., 'go north'
        # use lexicon.py's "scan" function to get a list of pairs
        # e.g. [('verb', 'go'), ('direction', 'north')]
        parsed_wordlist = scan(input)
        print parsed_wordlist
        
        parsed_sentence = parse_sentence(parsed_wordlist) # parse that sucker!
        # now the wordlist is a complicated Sentence object of some kind
        # but it has subject, verb, and object properties which are useful
        
        
        # parse player movement commands
        
        # if the player wants to go somewhere,
        if parsed_sentence.verb == ('go'):
        
            # make the player go where they wanna go!
            destination = parsed_sentence.object # object of sentence will be a
            room = travelto(room, destination)   # direction; go to it!
            output = room
        
        
        # parse player look commands
        
        # if the player wants to look at or examine something,
        if parsed_sentence.verb == ('look'):
        
            # make them look at the room they're in!
            print room.longdesc
            room_inventory = room.name + "_inv"
            print "In the room you see: "
            for i in items[room_inventory]:
                    print descriptions[i]
            output = room
            
            # (later I need to add functionality so they can also look at items,
            # possibly their own inventory, details in the room, etc)
        
        
        # parse player take commands
        
        # if the player wants to take something,
        if parsed_sentence.verb == ('take'):
        
            # figure out what they want to take!
            obj_taking = parsed_sentence.object
            inv_from = room.name + "_inv"
            print "taking " + obj_taking + " from " + inv_from
            
            # make sure that is a thing they can take      # this bit of code
            if obj_taking not in items[inv_from]:          # could be refactored
                # if it's not takable, print an error      # too, into inventory
                print "You can't take that."
                
            else: # if it's all good, put that thing in their inventory!
                move(items, obj_taking, inv_from, 'player_inv')
                print "Player inventory now contains: "
                for i in items['player_inv']:
                    print descriptions[i]
            
            output = room
        
        
        # if they're trying to drop something,
        if parsed_sentence.verb == ('drop'):
            
            # figure out what they want to drop!
            obj_dropping = parsed_sentence.object
            inv_to = room.name + "_inv"
            print "dropping " + obj_dropping + " into " + inv_to
            
            # make sure that is a thing they can drop      # could be refactored
            if obj_dropping not in items['player_inv']:
                # if it's not droppable, print an error
                print "You have to have something before you can drop it."
                
            else: # if it's all good, put that thing in their inventory!
                move(items, obj_dropping, 'player_inv', inv_to)
                print "Player inventory now contains: "
                for i in items['player_inv']:
                    print descriptions[i]
            
            output = room
        
        # if they're trying to use something,
        if parsed_sentence.verb == ('use'):
        
            # figure out what they want to use! then use it!
            obj_using = parsed_sentence.obj
            
            use(obj_using) # use is defined in inventory.py
            
            output = room
        
        # if they're trying to give something,
            # make sure there is someone to give it to
                # (even if parser thinks robot is indirect object, assume it's robot)
                # (maybe just check that they're in the entrance?)
            # take it out of their inventory and give it to the robot!
                # should have a separate function for robot responses
                # (most of the time the robot will ignore/reject items?)
            # if it's not in their inventory,
                # check if it's a cute easter egg; if so,
                    # return the easter egg result
                # else,
                    # return the error: "You can't give what you don't have!"
        
        # if they're trying to check their inventory,
            # print their inventory
    
    print "output: " + output.name
    return output
    
# code from inventory.py that belongs here:

# This is how I "ran" the inventory within each room before
# How can I 'centralize' this code here?
#
#        elif action == "inv":
#            print "You look at your inventory. "
#            for i in items['player_inv']:
#                print "You see" + descriptions[i] # prints the description of
#            return 'front_desk'                   # the item named 'i'
#        elif action == "take":
#            print "What do you want to take?"
#            item_to_take = raw_input("> ")
#            if item_to_take in items['front_desk_inv']:
#                move(item_to_take,'front_desk_inv','player_inv')
#                return 'front_desk'
#            else:
#                print "You can't take that."
#                return 'front_desk'
#        elif action == "give":
#            print "What do you want to give to the robot?"
#            item_to_give = raw_input("> ")
#            if item_to_give == 'bedtime story':
#                print "The robot reads the bedtime story and falls peacefully asleep."
#                return 'exit'
#            elif item_to_give == 'love':
#                print "The power of love saves the day! You and the robot live happily ever after."
#                return 'exit'
#            if item_to_give in items['player_inv']:
#                move(item_to_give,'player_inv', 'front_desk_inv')
#                return 'front_desk'
#            else:
#                print "You can't give that."
#                return 'front_desk'