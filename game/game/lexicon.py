# this function will parse each word in the sentence into a tuple
# and then put all those tuples in a bucket for future use
def scan(sentence):
    bucket = []
    
    words = sentence.split()
    
    for word in words:
        bucket.append(parse(word))
    
    return bucket

# this function checks for numbers and returns them as tuples
# because it's the last thing the parser checks, it also gives up
# on the whole parsing attempt if it doesn't find a number
def convert_number(word):
    try:
        return ('number', int(word))
    except ValueError:
        return ('error', word)

# this function compares a word against the lexicon
def parse_word(word):
# check that there's actually a word
    if word == None:
        return ('error', word)
# parse the directions
    elif word in ["north", "North", "N", "n"]:
        return ('direction', 'north')
    elif word in ["south", "South", "S", "s"]:
        return ('direction', 'south')
    elif word in ["east", "East", "E", "e"]:
        return ('direction', 'east')
    elif word in ["west", "West", "W", "w"]:
        return ('direction', 'west')
# parse the verbs
    elif word in ["go", "Go", "run", "Run"]:
        return ('verb', 'go')
    elif word in ["give", "Give"]:
        return ('verb', 'give')
    elif word in ["take", "Take"]:
        return ('verb', 'take')
    elif word in ["drop", "Drop", "put down", "Put down"]:
        return ('verb', 'drop')
# parse the nouns
    elif word in ["robot", "Robot", "bot", "librarian", "Librarian"]:
        return ('noun', 'robot')
    elif word in ["book", "Book", "stories", "Stories"]:
        return ('noun', 'book')
# parse the stopwords
    elif word in ["the", "The"]:
        return ('stop', 'the')
    elif word in ["in", "In"]:
        return ('stop', 'in')
    elif word in ["of", "Of"]:
        return ('stop', 'of')
# check if it's a number, and if not, give up
    else:
       return convert_number(word)