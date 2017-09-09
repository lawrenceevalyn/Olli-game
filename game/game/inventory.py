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

    
# Initial distribution of items in various inventories

items = { # inv names need to be room name + _inv (see map for room names)
    'entrance_inv' : ['robot', 'door', 'pencils', 'scanner'],
    'stacks_inv' : ['bedtime story', 'fairytales', 'rhymes', 'encyclopedia'],
    'lab_inv' : ['USB stick', 'cable', 'mousepads (36)', 'trash can'],
    'bathroom_inv' : ['water', 'lipstick'],
    'player_inv' : ['lint', 'library card'],
    'closet_inv' : ['teddy bear', 'broom', 'paper towels'],
    'the_void' : [] # this is so I can make the water go away when player cleans
    # also a place to store intangibles that the player can nonetheless give?
    }


# Functions to do stuff with the items

def move(dict, item, inv_from, inv_to):
    # will move the item between the lists in the items dict
    dict[inv_from].remove(item)
    dict[inv_to].append(item)