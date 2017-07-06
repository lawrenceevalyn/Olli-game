class ParserError(Exception):
    pass

# First there are a lot of functions that have to do with turning the input
# into sentences
# (why doesn't this use the lexicon???)

# Sentences have the attributes subject, verb, object
# (NOT subj, verb, obj!)
class Sentence(object):

    def __init__(self, subj, verb, obj):
        # remember we take ('noun', 'robot') tuples and convert them
        self.subject = subj[1] # i.e., the subject will be 'robot'
        self.verb = verb[1]
        self.object = obj[1]

def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None

def match(word_list, expecting):
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
    # take in the player input somehow
    
    inputSentence = parse_sentence(input)
    
    if inputSentence.verb == ('go'):
        # make the player go where they wanna go!
        output = "make player go north now"
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

parse_input([('verb','go'), ('direction','north')])