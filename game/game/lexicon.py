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
    elif word in ["take", "Take", "pick", "Pick"]:
        return ('verb', 'take')
    elif word in ["drop", "Drop", "put", "Put"]:
        return ('verb', 'drop')
    elif word in ["look", "Look", "examine", "Examine"]:
        return ('verb', 'look')
    elif word in ["use", "Use"]:
        return ('verb', 'use')

# parse the nouns
    elif word in ["room", "Room", "stacks", "lab", "bathroom"]:
        return ('noun', 'room')
    elif word in ["pencils", "Pencils", "pencil", "Pencil"]:
        return ('noun', 'pencils')
    elif word in ["lint", "Lint"]:
        return ('noun', 'lint')
    elif word in ["robot", "Robot", "librarian", "Librarian"]:
        return ('noun', 'robot')
    elif word in ["door", "Door"]:
        return ('noun', 'door')
    elif word in ["scanner", "Scanner"]:
        return ('noun', 'scanner')
    elif word in ["story", "Story", "book", "Book", "encyclopedia", "Encyclopedia"]:
        return ('noun', 'book') # I probably want to remove the book variety
    elif word in ["usb", "USB"]: # just so player doesn't have to play "hunt
        return ('noun', 'USB stick') # the adjective" to grab the right thing
    elif word in ["cable", "Cable"]:
        return ('noun', 'cable')
    elif word in ["mousepad", "Mousepad"]:
        return ('noun', 'mousepad')
    elif word in ["trash", "Trash"]:
        return ('noun', 'trash can')
    elif word in ["water", "Water", "spill", "Spill", "puddle", "Puddle"]:
        return ('noun', 'water')
    elif word in ["paper", "Paper", "towel", "Towel", "towels", "Towels", "roll", "roll"]:
        return ('noun', 'paper towels')
    elif word in ["card", "Card"]:
        return ('noun', 'library card')
    elif word in ["broom", "Broom"]:
        return ('noun', 'broom')
    elif word in ["lipstick", "Lipstick"]:
        return ('noun', 'lipstick')
    elif word in ["door", "Door"]:
        return ('noun', 'door')
    elif word in ["teddy", "Teddy", "bear", "Bear"]:
        return ('noun', 'teddy bear')
    elif word in ["testobject"]:
        return ('noun', 'testobject')
    elif word in ["love", "friendship", "affection"]:
        return ('noun', 'love')
    
# parse the stopwords
    elif word in ["the", "The", "a", "A", "an", "An"]:
        return ('stop', 'article')
    elif word in ["in", "In","of", "Of","at", "At",'around', 'Around',"to", "To","down", "Down","back", "Back","up", "Up"]:
        return ('stop', 'preposition')
    elif word in ["barcode", "Barcode",]: # "stop" adjectives too
        return ('stop', 'barcode')        # since I won't parse them
    elif word in ["library", "Library"]:
        return ('stop', 'library')

# check if it's a number, and if not, give up
    else:
       return convert_number(word)