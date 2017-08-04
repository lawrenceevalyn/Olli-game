from nose.tools import *
from game import parser
from game.map import *
from game.lexicon import scan

def test_sentence_parser():
    result = parser.parse_sentence([('verb','go'), ('direction','north')])
    assert_equal(result.subject, "player")
    assert_equal(result.verb, "go")
    assert_equal(result.object, "north")
    
    result = parser.parse_sentence(scan("go north"))
    assert_equal(result.subject, "player")
    assert_equal(result.verb, "go")
    assert_equal(result.object, "north")

def test_input_parser():
    
    # test multiple ways to express "go south"
    # don't have to test the whole map, because map_tests will do that;
    # but do have to test many ways of saying the same action
    
    result = parser.parse_input("s", entrance)
    assert_equal(result, stacks)
    
    result = parser.parse_input("go south", entrance)
    assert_equal(result, stacks)
    
    result = parser.parse_input("Go South", entrance)
    assert_equal(result, stacks)
    
    result = parser.parse_input("run south", entrance)
    assert_equal(result, stacks)
    
    
    # test parsing the other directions
    
    result = parser.parse_input("go north", entrance)
    assert_equal(result, exit) # this one might be weird?
    
    result = parser.parse_input("go east", entrance)
    assert_equal(result, lab)
    
    result = parser.parse_input("go west", entrance)
    assert_equal(result, bathroom)
    
    
    # test looking at the room
    
    result = parser.parse_input("look at room", entrance)
    assert_equal(result, entrance)
    
    result = parser.parse_input("L", entrance)
    assert_equal(result, entrance)
    
    result = parser.parse_input("look", entrance)
    assert_equal(result, entrance)
    
    result = parser.parse_input("look around", entrance)
    assert_equal(result, entrance)
    
    result = parser.parse_input("look at stacks", entrance)
    assert_equal(result, entrance)
    
    result = parser.parse_input("examine room", entrance)
    assert_equal(result, entrance)
    
    # test taking
#    result = parser.parse_input([('verb','take'), ('noun','book')])
#    assert_equal(result, "make player take the book")
    
    
    # test giving
#    result = parser.parse_input([('verb','give'), ('noun','book')])
#    assert_equal(result, "make player give the book to the robot")
    
    
    # test dropping
#    result = parser.parse_input([('verb','drop'), ('noun','book')])
#    assert_equal(result, "make player drop the book")
    

def test_errors():
    assert_raises(parser.ParserError, parser.parse_verb, ('noun','robot'))
    
    
    # don't move the player if they try to go down invalid path
    
    result = parser.parse_input("s", lab) 
    assert_equal(result, lab)
    
    result = parser.parse_input("go south", lab)
    assert_equal(result, lab)
    
    result = parser.parse_input("go east", lab)
    assert_equal(result, lab)
    
    result = parser.parse_input("go north", bathroom)
    assert_equal(result, bathroom)
    
    result = parser.parse_input("go west", bathroom)
    assert_equal(result, bathroom)