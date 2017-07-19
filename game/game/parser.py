from lexicon import *
from map import *

class ParserError(Exception): # I guess this is here so that if there are errors
    pass                      # later, they display the error messages I wrote?

# First there are a lot of functions that have to do with turning the input
# into sentences
# (why doesn't this use the lexicon???)

# Sentences have the attributes subject, verb, object
# (NOT subj, verb, obj!)
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
        print "the room is: " + name.room
        next_room = room.go('north')
        print "the next room is: " + name.next_room
        if next_room == "invalid path":
            print "You can't go that way"
        else:
            room = next_room
            print "the room is now: " + name.room
        output = room
    if shortcut in ["E", "e"]:
        next_room = room.go('east')
        if next_room == "invalid path":
            print "You can't go that way"
        else:
            room = next_room
        output = room
    if shortcut in ["S", "s"]:
        next_room = room.go('south')
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
        output = parse_shortcuts(input, room)
    
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
        if parsed_sentence.verb == ('go'):
            # make the player go where they wanna go!
            print "The player wants to travel!"
            if parsed_sentence.object == ('north'):
                print "They specified the direction north!"
                next_room = room.go('north')
                if next_room == "invalid path":    # I feel like there should be
                    print "You can't go that way"  # a way not to just repeat
                else:                              # this code eight times, but
                    room = next_room               # *shrug emoji*
                output = room
            elif parsed_sentence.object == ('east'):
                print "They specified the direction east!"
                next_room = room.go('east')
                if next_room == "invalid path":
                    print "You can't go that way"
                else:
                    room = next_room
                output = room
            elif parsed_sentence.object == ('south'):
                print "They specified the direction south!"
                next_room = room.go('south')
                if next_room == "invalid path":
                    print "You can't go that way"
                else:
                    room = next_room
                output = room
            elif parsed_sentence.object == ('west'):
                print "They specified the direction west!"
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
        if parsed_sentence.verb == ('look'):
            print room.longdesc # right now this just assumed they look at
            # the room, but could just as easily be looking at inventory or an
            # individual object -- implement with parser if-clauses!
            output = room
        
        # if they're trying to take something,
            # put that thing in their inventory!
            # if it's not takable, print an error
        
        # if they're trying to give something,
            # take it out of their inventory and give it to the robot!
            # if it's not in their inventory,
                # check if it's a cute easter egg; if so,
                    # return the easter egg result
                # else,
                    # return the error: "You can't give what you don't have!"
        
        # if they're trying to drop something,
            # take it out of their inventory and add it to the room inventory
            # if it's not in their inventory, print an error
        
        # if they're trying to check their inventory,
            # print their inventory
        
    print "output: "
    print output
    return output