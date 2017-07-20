from nose.tools import *
from game import inventory
from game.inventory import *

def test_items():
    # test that the pencils have the right description
    assert_equal(descriptions['pencils'], "a jar of tiny pencils")
    # (really this is a test of my ability to understand how that code works)
    
    # test that the items start out in the right rooms
    assert_equal(items['front_desk_inv'], ['robot', 'door', 'pencils', 'scanner'])
    
    assert_equal(items['stacks_inv'], ['bedtime story', 'fairytales', 'rhymes', 'encyclopedia'])
    
    assert_equal(items['lab_inv'], ['USB stick', 'cable', 'mousepads (36)', 'trash can'])
    
    assert_equal(items['bathroom_inv'], ['water', 'lipstick'])
    
    assert_equal(items['player_inv'], ['lint', 'library card'])
    
    assert_equal(items['closet_inv'], ['teddy bear', 'broom', 'paper towels'])
    
    assert_equal(items['the_void'], [])

def test_move():
    pass
    # test the move function