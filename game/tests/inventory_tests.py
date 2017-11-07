from nose.tools import *
from game import inventory
from game.inventory import *
from game.inventory import items

def test_items():
    # test that the pencils have the right description
    assert_equal(descriptions['pencils'], "a jar of tiny pencils")
    # (really this is a test of my ability to understand how that code works)
    
    # test that the items start out in the right rooms
    assert_equal(items['entrance_inv'], ['robot', 'door', 'pencils', 'scanner'])
    
    assert_equal(items['stacks_inv'], ['bedtime story', 'fairytales', 'rhymes', 'encyclopedia'])
    
    assert_equal(items['lab_inv'], ['USB stick', 'cable', 'mousepads (36)', 'trash can'])
    
    assert_equal(items['bathroom_inv'], ['water', 'lipstick'])
    
    assert_equal(items['player_inv'], ['lint', 'library card'])
    
    assert_equal(items['closet_inv'], ['teddy bear', 'broom', 'paper towels'])
    
    assert_equal(items['the_void'], ['love'])

def test_move():
    test_items = {               # set up an inventory to test moving around
        'inv_from' : ['pencils', 'robot'],
        'inv_to' : ['broom']
        }
    
    assert_equal(test_items['inv_from'], ['pencils', 'robot']) # check that it's
    assert_equal(test_items['inv_to'], ['broom'])              # all as planned
    
    move(test_items, 'pencils', 'inv_from', 'inv_to') # move stuff around!
    
    assert_equal(test_items['inv_from'], ['robot'])          # no teardown bc
    assert_equal(test_items['inv_to'], ['broom', 'pencils']) # it's a test inv


def test_clean_bathroom():
    move(items, 'paper towels', 'closet_inv', 'player_inv')        # setup
    
    assert 'paper towels' in items['player_inv']
    assert 'water' in items['bathroom_inv']
    assert 'paper towels' not in items['bathroom_inv']
    
    useobj(bathroom, 'paper towels')
    
    assert 'paper towels' in items['the_void']
    assert 'paper towels' not in items['player_inv']
    assert 'paper towels' in items['the_void']
    assert 'paper towels' not in items['player_inv']
    
    move(items, 'paper towels', 'the_void', 'closet_inv')         # teardown
    move(items, 'water', 'the_void', 'bathroom_inv')

# test taking

def setup_take(): # these will run before and after the tests that call them,
    items["entrance_inv"].append("testobject") # because otherwise the changes
def teardown_take():                           # made to invs will persist thru
    items["player_inv"].remove("testobject")   # ALL the tests, which causes
                                               # total crazy nonsense.
@with_setup(setup_take, teardown_take)
def test_take():
    assert 'testobject' in items['entrance_inv']
    assert 'testobject' not in items['player_inv']
    
    takeobj(entrance, 'testobject')
    
    assert 'testobject' in items['player_inv']
    assert 'testobject' not in items['entrance_inv']

@with_setup(setup_take, teardown_take) # re-running same test proves that tests
def test_retake():                     # are actually running independently!
    assert 'testobject' in items['entrance_inv']
    assert 'testobject' not in items['player_inv']
    
    takeobj(entrance, 'testobject')
    
    assert 'testobject' in items['player_inv']
    assert 'testobject' not in items['entrance_inv']

# need a LOT more tests to make sure player can't take untakable things!!


# test dropping

def setup_drop():
    items["player_inv"].append("testobject")   # conjunction with taking because
def teardown_drop():                           # setup/teardown makes them
    items["entrance_inv"].remove("testobject") # independent now!! :D

@with_setup(setup_drop, teardown_drop)
def test_drop():
    assert 'testobject' in items['player_inv']
    assert 'testobject' not in items['entrance_inv']
    
    dropobj(entrance, 'testobject')
    
    assert 'testobject' in items['entrance_inv']
    assert 'testobject' not in items['player_inv']


# test giving

def setup_give():
    items["player_inv"].append("testobject")
def teardown_give():
    items["robot_inv"].remove("testobject")

@with_setup(setup_give, teardown_give)
def test_give():
    assert 'testobject' in items['player_inv']
    assert 'testobject' not in items['robot_inv']
    
    giveobj(entrance, 'testobject')
    
    assert 'testobject' in items['robot_inv']
    assert 'testobject' not in items['player_inv']

def setup_give_bear():
    items["player_inv"].append("teddy bear")
def teardown_give():
    items["robot_inv"].remove("teddy bear")

@with_setup(setup_give_bear, teardown_give_bear)
def test_give_bear():
    assert 'teddy bear' in items['player_inv']
    assert 'teddy bear' not in items['robot_inv']
    assert config.robot_status == "sad"
    
    giveobj(entrance, 'testobject')
    
    assert 'teddy bear' in items['robot_inv']
    assert 'teddy bear' not in items['player_inv']
    config.robot_status == "wantsstory"
