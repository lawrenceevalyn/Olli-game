from sys import exit

class Room(object):

    def enter(self):
        print "This isn't a real room yet. You should fix that."
        exit(1)

# this is what will run the game
class GameEngine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('exit')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter() # enter will return a room
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()


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
    'water' : "There is water.",
    'paper towels' : "There are paper towels.",
    'broom' : "There is a broom.",
    'lipstick' : "There is a half-used tube of lipstick in a fetching shade of coral.",
    'lint' : "There is lint.",
    'library card' : "There is a library card with a studious photograph of yourself.",
    }
    
items = {
    'front_desk_inv' : ['robot', 'door', 'pencils', 'scanner'],
    'stacks_inv' : ['bedtime story', 'fairytales', 'rhymes', 'encyclopedia'],
    'lab_inv' : ['USB stick', 'cable', 'mousepads (36)', 'trash can'],
    'bathroom_inv' : ['water', 'paper towels', 'broom', 'lipstick'],
    'player_inv' : ['lint', 'library card'],
    }

def move(item, inv_from, inv_to):
    # will move the item between the lists in the items dict
    items[inv_from].remove(item)
    items[inv_to].append(item)

class FrontDesk(Room):

    def enter(self):
        print "You are at the front desk. To leave the library you have to pass the distressed robot librarian. The exit is North. The stacks are South. The computer lab is East. The bathroom is West."
        
        action = raw_input("> ")
        
        if action == "N":
            print "Oh, I guess you can just ignore the robot's distress and go."
            return 'exit'
        elif action == "S":
            return 'stacks'
        elif action == "E":
            return 'computer_lab'
        elif action == "W":
            return 'bathroom'
        elif action == "look":
            print "You look around the room. "
            for i in items['front_desk_inv']:
                print descriptions[i]
            return 'front_desk'
        elif action == "inv":
            print "You look at your inventory. "
            for i in items['player_inv']:
                print descriptions[i]
            return 'front_desk'
        elif action == "take":
            print "What do you want to take?"
            item_to_take = raw_input("> ")
            if item_to_take in items['front_desk_inv']:
                move(item_to_take,'front_desk_inv','player_inv')
                return 'front_desk'
            else:
                print "You can't take that."
                return 'front_desk'
        elif action == "give":
            print "What do you want to give to the robot?"
            item_to_give = raw_input("> ")
            if item_to_give == 'bedtime story':
                print "The robot reads the bedtime story and falls peacefully asleep."
                return 'exit'
            elif item_to_give == 'love':
                print "The power of love saves the day! You and the robot live happily ever after."
                return 'exit'
            if item_to_give in items['player_inv']:
                move(item_to_give,'player_inv', 'front_desk_inv')
                return 'front_desk'
            else:
                print "You can't give that."
                return 'front_desk'
        else:
            print "I didn't understand that. I understand N, E, S, W, look, inv, take, and give."
            return 'front_desk'


class Stacks(Room):

    def enter(self):
        print "You are in the stacks. The front desk is North."
        
        action = raw_input("> ")
        
        if action == "N":
            return 'front_desk'
        elif action == "S":
            print "There's no exit that way."
            return 'stacks'
        elif action == "E":
            print "There's no exit that way."
            return 'stacks'
        elif action == "W":
            print "There's no exit that way."
            return 'stacks'
        elif action == "look":
            print "You look around the room. "
            for i in items['stacks_inv']:
                print descriptions[i]
            return 'stacks'
        elif action == "inv":
            print "You look at your inventory. "
            for i in items['player_inv']:
                print descriptions[i]
            return 'stacks'
        elif action == "take":
            print "What do you want to take?"
            item_to_take = raw_input("> ")
            if item_to_take in items['stacks_inv']:
                move(item_to_take,'stacks_inv','player_inv')
                return 'stacks'
            else:
                print "You can't take that."
                return 'stacks'
        elif action == "give":
            print "What do you want to put in this room?"
            item_to_give = raw_input("> ")
            if item_to_give in items['player_inv']:
                move(item_to_give,'player_inv', 'stacks_inv')
                return 'stacks'
            else:
                print "You can't give that."
                return 'stacks'
        else:
            print "I didn't understand that. I understand N, E, S, W, look, inv, take, and give."
            return 'stacks'


class ComputerLab(Room):

    def enter(self):
        print "You are in the computer lab. The front desk is West."
        
        action = raw_input("> ")
        
        if action == "N":
            print "There's no exit that way."
            return 'computer_lab'
        elif action == "S":
            print "There's no exit that way."
            return 'computer_lab'
        elif action == "E":
            print "There's no exit that way."
            return 'computer_lab'
        elif action == "W":
            return 'front_desk'
        elif action == "look":
            print "You look around the room. "
            for i in items['lab_inv']:
                print descriptions[i]
            return 'computer_lab'
        elif action == "inv":
            print "You look at your inventory. "
            for i in items['player_inv']:
                print descriptions[i]
            return 'computer_lab'
        elif action == "take":
            print "What do you want to take?"
            item_to_take = raw_input("> ")
            if item_to_take in items['lab_inv']:
                move(item_to_take,'lab_inv','player_inv')
                return 'computer_lab'
            else:
                print "You can't take that."
                return 'computer_lab'
        elif action == "give":
            print "What do you want to put in this room?"
            item_to_give = raw_input("> ")
            if item_to_give in items['player_inv']:
                move(item_to_give,'player_inv', 'lab_inv')
                return 'computer_lab'
            else:
                print "You can't give that."
                return 'computer_lab'
        else:
            print "I didn't understand that. I understand N, E, S, W, look, inv, take, and give."
            return 'computer_lab'


class Bathroom(Room):

    def enter(self):
        print "You are in the bathroom. The front desk is East."
        
        action = raw_input("> ")
        
        if action == "N":
            print "There's no exit that way."
            return 'bathroom'
        elif action == "S":
            print "There's no exit that way."
            return 'bathroom'
        elif action == "E":
            return 'front_desk'
        elif action == "W":
            print "There's no exit that way."
            return 'bathroom'
        elif action == "look":
            print "You look around the room. "
            for i in items['bathroom_inv']:
                print descriptions[i]
            return 'bathroom'
        elif action == "inv":
            print "You look at your inventory. "
            for i in items['player_inv']:
                print descriptions[i]
            return 'bathroom'
        elif action == "take":
            print "What do you want to take?"
            item_to_take = raw_input("> ")
            if item_to_take in items['bathroom_inv']:
                move(item_to_take,'bathroom_inv','player_inv')
                return 'bathroom'
            else:
                print "You can't take that."
                return 'bathroom'
        elif action == "give":
            print "What do you want to put in this room?"
            item_to_give = raw_input("> ")
            if item_to_give in items['player_inv']:
                move(item_to_give,'player_inv', 'bathroom_inv')
                return 'bathroom'
            else:
                print "You can't give that."
                return 'bathroom'
        else:
            print "I didn't understand that. I understand N, E, S, W, look, inv, take, and give."
            return 'bathroom'


class Exit(Room):

    def enter(self):
        print "You exit the library! Now you can go home. Well done!"


class Map(object):

    scenes = {
        'front_desk': FrontDesk(),
        'stacks': Stacks(),
        'computer_lab': ComputerLab(),
        'bathroom': Bathroom(),
        'exit': Exit(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

# this is what causes the game to play
a_map = Map('front_desk')
a_game = GameEngine(a_map)
a_game.play()