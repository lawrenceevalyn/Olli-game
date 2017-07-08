from lexicon import *

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
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")

def parse_object(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)
    
    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next.")

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

# After all of that sentence business, now we can parse the intended action!!

def parse_input(input):
    # take in the player input, e.g. "go north"
    print "input: " + input
    
    # use lexicon.py's "scan" function to get a list of pairs
    # e.g. [('verb', 'go'), ('direction', 'north')]
    parsed_wordlist = scan(input)
    print "parsed_wordlist: "
    print parsed_wordlist
    
    parsed_sentence = parse_sentence(parsed_wordlist) # parses parts of speech
    # now the sentence is a complicated Sentence object of some kind
    # but it has subject, verb, and object properties which are useful
    print "parsed_sentence: "
    print parsed_sentence
    
    if parsed_sentence.verb == ('go'):
        # make the player go where they wanna go!
        print "The player wants to travel!"
        if parsed_sentence.object == ('north'):
            print "They specified the direction north!"
            output = "make player go north now"
        else:
            print "That's not somewhere they can go."
            output = "Can't go there"
        
        print "output: " + output
        return output
    
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
    
    # if they're trying to look around,
        # print the room's long description and its inventory

parse_input("go north")