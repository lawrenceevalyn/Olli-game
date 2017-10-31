from lexicon import *
from map import *
from inventory import *
from robot import *
import config

class ParserError(Exception): # I guess this is here so that if there are errors
    pass                      # later, they display the error messages I wrote?

# First there are a lot of functions that turn the input into sentences
# (Doesn't have to call the lexicon directly, because the lexicon was already
# used to give each word its part-of-speech buddy)

# Sentences have the attributes verb, object, indirectobj 
# (NOT verb, obj, ind!)
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
    
    if next_word == 'noun':
        return match(word_list, 'noun')
    else:
        return ('noun', 'implied indirect object')


def parse_sentence(word_list):
    verb = parse_verb(word_list)
    obj = parse_object(word_list)
    ind = parse_indobject(word_list)
    
    return Sentence(verb, obj, ind)

# this list defines the "shortcut" commands that can skip the parsing process
shortcuts_list = ('n', 'e', 's', 'w', 'l', 'x', 'i', 'N', 'E', 'S', 'W', 'L', 'X', 'I', 'win')

def parse_shortcuts(shortcut, room):

    # parse looking shortcuts
    if shortcut in ["l", "L", "x", "X"]:
        print room.longdesc
        print "The room contains:"
        printinv(room.name+'_inv')
        output = room
        
    elif shortcut in ["i", "I"]:
        print "You have:"
        printinv('player_inv') # defined in inventory.py
        output = room
    
    elif shortcut == 'win':
        updaterobot("win")
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
            printinv(room.name+'_inv')
            output = room
            
            # (later I need to add functionality so they can also look at items,
            # possibly their own inventory, details in the room, etc)
        
        
        # parse player take commands
        
        # if the player wants to take something,
        if parsed_sentence.verb == ('take'):
        
            # figure out what they want to take!
            obj_taking = parsed_sentence.object
            takeobj(room, obj_taking)
            
            output = room
        
        
        # if they're trying to drop something,
        if parsed_sentence.verb == ('drop'):
            
            # figure out what they want to drop!
            obj_dropping = parsed_sentence.object
            dropobj(room, obj_dropping)
            
            output = room
        
        # if they're trying to use something,
        if parsed_sentence.verb == ('use'):
        
            # figure out what they want to use! then use it!
            obj_using = parsed_sentence.object
            print "using object: " + obj_using
            useobj(room, obj_using) # useobj is defined in inventory.py
            
            output = room
        
        # if they're trying to give something,
        if parsed_sentence.verb == ('give'):
            obj_giving = parsed_sentence.object
            print "giving object: " + obj_giving
            giveobj(room, obj_giving) # giveobj is defined in inventory.py
            output = room             # it checks for someone to give to
        
        # if they're trying to check their inventory,
            # print their inventory
            
        # if none of the above happened, give up in confusion
        else:
            print "That doesn't make sense."
            output = room
    
    if output == exit:
        print "You're about to leave the library!"
        print "Robot status: " + config.robot_status
        checkending()
        
#   print "output: " + output.name
    return output