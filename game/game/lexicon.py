# this function will parse each word in the sentence into a tuple
# and then put all those tuples in a bucket for future use
def scan(sentence):
    bucket = []
    
    words = sentence.split()
    
    for word in words:
        bucket.append(parse_word(word))
    
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
    elif word in ["go", "Go", "run", "Run", "walk", "Walk", "move", "Move"]:
        return ('verb', 'go')
    elif word in ["give", "Give"]:
        return ('verb', 'give')
    elif word in ["take", "Take"]:
        return ('verb', 'take')
    elif word in ["drop", "Drop", "put down", "Put down"]:
        return ('verb', 'drop')
    elif word in ["look", "Look", "examine", "Examine"]:
        return ('verb', 'look')
# parse the nouns
    elif word in ["room", "Room"]:
        return ('noun', 'room')
    elif word in ["pencils", "Pencils", "pencil", "Pencil"]:
        return ('noun', 'pencils')
    elif word in ["lint", "Lint"]:
        return ('noun', 'lint')
# parse the stopwords
    elif word in ["the", "The"]:
        return ('stop', 'the')
    elif word in ["in", "In"]:
        return ('stop', 'in')
    elif word in ["of", "Of"]:
        return ('stop', 'of')
    elif word in ["at", "At"]:
        return ('stop', 'at')
    elif word in ['around', 'Around']:
        return ('stop', 'around')
# check if it's a number, and if not, give up
    else:
       return convert_number(word)