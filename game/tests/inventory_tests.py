from nose.tools import *
from game import inventory
from game.inventory import *
from game.inventory import items
from game import parser

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
    
    assert_equal(items['the_void'], [])

def test_move():
    test_items = {               # set up an inventory to test moving around
        'inv_from' : ['pencils', 'robot'],
        'inv_to' : ['broom']
        }
    
    assert_equal(test_items['inv_from'], ['pencils', 'robot'])
    assert_equal(test_items['inv_to'], ['broom'])
    
    # move stuff around!
    
    move(test_items, 'pencils', 'inv_from', 'inv_to')
    
    assert_equal(test_items['inv_from'], ['robot'])          # no teardown bc
    assert_equal(test_items['inv_to'], ['broom', 'pencils']) # it's a test inv


def test_clean_bathroom():
    move(items, 'paper towels', 'closet_inv', 'player_inv')        # setup
    
    assert 'paper towels' in items['player_inv']
    assert 'water' in items['bathroom_inv']
    assert 'paper towels' not in items['bathroom_inv']
    parser.parse_input("use towel", bathroom)
    assert 'paper towels' in items['the_void']
    assert 'paper towels' not in items['player_inv']
    assert 'paper towels' in items['the_void']
    assert 'paper towels' not in items['player_inv']
    
    move(items, 'paper towels', 'the_void', 'closet_inv')         # teardown
    move(items, 'water', 'the_void', 'bathroom_inv')

def test_give():
