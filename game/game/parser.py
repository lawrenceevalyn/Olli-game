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

    def __init__(self, subj, verb, obj):
        #  we take ('noun', 'robot') tuples and get just the second word
        self.subject = subj[1] # i.e., the subject will be 'robot'
        self.verb = verb[1]
        self.object = obj[1]

def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None

def match(word_list, expecting): # I have no idea what this does
    if word_list:
        word = word_list.pop(0)
        
        if word[0] == expecting:
            return word
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
        raise ParserError("Expected a verb next.") # only gets parsed once

def parse_object(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)
    
    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        return ('noun', 'implied object')

def parse_subject(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)
    
    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'verb':
        return ('noun', 'player')
    else:
        return ParserError("Expected a verb next.")

def parse_sentence(word_list):
    subj = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)
    
    return Sentence(subj, verb, obj)

# this list defines the "shortcut" commands that can skip the parsing process
shortcuts_list = ('n', 'e', 's', 'w', 'l', 'x', 'i', 'N', 'E', 'S', 'W', 'L', 'X', 'I')

def parse_shortcuts(shortcut, room):
    if shortcut in ["N", "n"]:
        print "the room is: " + room.name
        next_room = room.go('north')
        if next_room == "invalid path":
            print "Next room: " + next_room
            print "You can't go that way"
        else:
            print "The next room is: " + next_room.name
            room = next_room
            print "the room is now: " + room.name
        print "outside the if statement, the room is: " + room.name
        output = room
    if shortcut in ["E", "e"]:
        next_room = room.go('east')       # Man, these shortcuts really don't
        if next_room == "invalid path":   # make MY work shorter, since I have
            print "You can't go that way" # to type everything twice... and they
        else:                             # don't make the program run faster...
            room = next_room              # I guess what they "shortcut" around
        output = room                     # is me figuring out how to make the
    if shortcut in ["S", "s"]:            # parser gracefully understand inputs
        next_room = room.go('south')      # of only a single letter.
        if next_room == "invalid path":
            print "You can't go that way"
        else:
            room = next_room
        output = room
    if shortcut in ["W", "w"]:
        next_room = room.go('west')
        if next_room == "invalid path":
            print "You can't go that way"
        else:
            room = next_room
        output = room
    if shortcut in ["l", "L", "x", "X"]:
        print room.longdesc
        output = room
    
    return output # don't need to print output here, since this function only
                  # runs when parse_input calls it, and parse_input will print


# After all of that sentence business, now we can parse the intended action!!
def parse_input(input, room):
    
    room = room # apparently I have to say this so that anything works later
    
    # take in the player input, e.g. "go north"
    print "input: " + input
    
    # compare the input to a list of shortcuts; use shortcut parser if relevant
    if input in shortcuts_list:
        room = parse_shortcuts(input, room)
        output = room
        print "the output of the shortcut function in parse_input is: " + output.name
    
    else: # if it's not a shortcut, gotta actually parse it
    
        # use lexicon.py's "scan" function to get a list of pairs
        # e.g. [('verb', 'go'), ('direction', 'north')]
        parsed_wordlist = scan(input)
        print "parsed_wordlist: "
        print parsed_wordlist
        
        parsed_sentence = parse_sentence(parsed_wordlist) # parse that sucker!
        # now the wordlist is a complicated Sentence object of some kind
        # but it has subject, verb, and object properties which are useful
        
        
        # parse player movement commands
        
        # if the player wants to go somewhere,
        if parsed_sentence.verb == ('go'):
        
            # make the player go where they wanna go!
            if parsed_sentence.object == ('north'):
                next_room = room.go('north')
                if next_room == "invalid path":    # I feel like there should be
                    print "You can't go that way"  # a way NOT to just repeat
                else:                              # this code eight times, but
                    room = next_room               # *shrug emoji*
                output = room
            elif parsed_sentence.object == ('east'):
                next_room = room.go('east')
                if next_room == "invalid path":
                    print "You can't go that way"
                else:
                    room = next_room
                output = room
            elif parsed_sentence.object == ('south'):
                next_room = room.go('south')
                if next_room == "invalid path":
                    print "You can't go that way"
                else:
                    room = next_room
                output = room
            elif parsed_sentence.object == ('west'):
                next_room = room.go('west')
                if next_room == "invalid path":
                    print "You can't go that way"
                else:
                    room = next_room
                output = room
            else:
                print "That's not somewhere they can go."
                room = room
                output = room
        
        
        # parse player look commands
        
        # if the player wants to look at or examine something,
        if parsed_sentence.verb == ('look'):
        
            # make them look at the room they're in!
            print room.longdesc
            output = room
            
            # (later I need to add functionality so they can also look at items,
            # possibly their own inventory, details in the room, etc)
        
        
        # parse player give / take commands
        
        # if the player wants to take something,
        if parsed_sentence.verb == ('take'):
        
            # figure out what they want to take!
            obj_taking = parsed_sentence.object
            inv_from = room.name + "_inv"
            print "taking " + obj_taking + " from " + inv_from
            
            # make sure that is a thing they can take
            if obj_taking not in items[inv_from]:
                # if it's not takable, print an error
                print "You can't take that."
                
            else: # if it's all good, put that thing in their inventory!
                move(items, obj_taking, inv_from, 'player_inv')
                print "Player inventory now contains: "
                for i in items['player_inv']:
                    print descriptions[i]
            
            output = room
            
        # if they're trying to drop something,
            # take it out of their inventory and add it to the room inventory
            # if it's not in their inventory, print an error
        
        # if they're trying to use something,
            # what do I do?? maybe a function for trying to use items?
            # that checks if the item has a use within the room they're in?
            # or maybe it needs an indirect object?
        
        # if they're trying to give something,
            # make sure there is someone to give it to
                # (do I need to implement indirect objects for this??)
            # take it out of their inventory and give it to the robot!
                # should have a separate function for robot responses
            # if it's not in their inventory,
                # check if it's a cute easter egg; if so,
                    # return the easter egg result
                # else,
                    # return the error: "You can't give what you don't have!"
        
        # if they're trying to check their inventory,
            # print their inventory
   
    print "the room in the parse_input function is: " + room.name
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