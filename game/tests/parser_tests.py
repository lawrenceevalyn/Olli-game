from nose.tools import *
from game import parser
from game import map

def test_sentence_parser():
    result = parser.parse_sentence([('verb','go'), ('direction','north')])
    assert_equal(result.subject, "player")
    assert_equal(result.verb, "go")
    assert_equal(result.object, "north")

def test_input_parser():
    # test multiple ways to express "go north"
    result = parser.parse_input("go north", entrance)
    assert_equal(result, "make player go north now")
    
    result = parser.parse_input("Go North")
    assert_equal(result, "make player go north now")
    
    result = parser.parse_input("run north")
    assert_equal(result, "make player go north now")
    
    result = parser.parse_input("n")
    assert_equal(result, "make player go north now")
    
    # test parsing the other directions
    
    result = parser.parse_input("go south")
    assert_equal(result, "make player go south now")
    
    result = parser.parse_input("go east")
    assert_equal(result, "make player go east now")
    
    result = parser.parse_input("go west")
    assert_equal(result, "make player go west now")
    
    # test looking
    result = parser.parse_input("look at room")
    assert_equal(result, room.longdesc)
    
    result = parser.parse_input("L")
    assert_equal(result, room.longdesc)
    
    result = parser.parse_input("look")
    assert_equal(result, room.longdesc)
    
    result = parser.parse_input("look around")
    assert_equal(result, room.longdesc)
    
    result = parser.parse_input("look at stacks")
    assert_equal(result, room.longdesc)
    
    result = parser.parse_input("examine room")
    assert_equal(result, room.longdesc)
    
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