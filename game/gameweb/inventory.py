# All the items in the game, and the game's name for them

descriptions = {
    'robot' : "The robot librarian is distressed. It can't shut down. ",
    'door' : "You can see the door to the exit. If only you could go through it. ",
    'pencils' : "There is a jar of tiny pencils. ",
    'scanner' : "There is a barcode scanner. ",
    'bedtime story' : "There is a copy of Goodnight, Moon.",
    'fairytales' : "There is a heavy volume of scary fairytales.",
    'rhymes' : "There is a brightly-coloured book of children's rhymes.",
    'encyclopedia' : "There is a seven-volume encyclopedia of dinosaurs.",
    'USB stick' : "There is a mysterious USB stick.",
    'cable' : "There is a cable to connect a printer to something.",
    'mousepads (36)' : "There are thirty-six mousepads.",
    'trash can' : "There is a half-full trash can.",
    'water' : "There is water. You wonder if you should clean it up.",
    'paper towels' : "There are paper towels.",
    'broom' : "There is a broom.",
    'lipstick' : "There is a half-used tube of lipstick in a fetching shade of coral.",
    'lint' : "There is lint.",
    'library card' : "There is a library card with a studious photograph of yourself.",
    'teddy bear' : "There is a small toy, kind of like a bear."
    }

    
# Initial distribution of items in various inventories

items = {
    'front_desk_inv' : ['robot', 'door', 'pencils', 'scanner'],
    'stacks_inv' : ['bedtime story', 'fairytales', 'rhymes', 'encyclopedia'],
    'lab_inv' : ['USB stick', 'cable', 'mousepads (36)', 'trash can'],
    'bathroom_inv' : ['water', 'lipstick'],
    'player_inv' : ['lint', 'library card'],
    'closet_inv' : ['teddy bear', 'broom', 'paper towels']
    }


# Functions to do stuff with the items

def move(item, inv_from, inv_to):
    # will move the item between the lists in the items dict
    items[inv_from].remove(item)
    items[inv_to].append(item)
    

# This is how I "ran" the inventory within each room before
# How can I 'centralize' this code here?
#
#        elif action == "inv":
#            print "You look at your inventory. "
#            for i in items['player_inv']:
#                print descriptions[i]
#            return 'front_desk'
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